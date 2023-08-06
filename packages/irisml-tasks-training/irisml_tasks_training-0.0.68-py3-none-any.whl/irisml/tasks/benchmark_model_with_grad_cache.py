import contextlib
import copy
import dataclasses
import logging
import time
import torch
from irisml.tasks.train.build_dataloader import build_dataloader
from irisml.tasks.train.plugin_list import PluginList
from irisml.tasks.train.plugin_loader import load_plugin
from irisml.tasks.train_with_gradient_cache import GradientCachingMixin, GradientCachingTrainer
from irisml.tasks.benchmark_model import Task as BenchmarkModelTask

logger = logging.getLogger(__name__)


class Task(BenchmarkModelTask):
    """Benchmark a given model using a given dataset with grad caching. Useful for cases which require sub batching.

    Config:
        sub_batch_size (int)
    """
    VERSION = '0.0.1'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Config(BenchmarkModelTask.Config):
        sub_batch_size: int = 1
        grad_caching: bool = True

    def execute(self, inputs):
        plugins = PluginList([load_plugin(p, self.context) for p in self.config.plugins])
        device = self._get_device()
        self.device = device
        dataloader = build_dataloader(inputs.dataset, inputs.transform, batch_size=self.config.batch_size, shuffle=False, drop_last=False)
        forward_time_all = []
        backward_time_all = []
        prediction_time_all = []

        model = copy.deepcopy(inputs.model)
        if device.type == 'cuda':
            torch.cuda.reset_peak_memory_stats(device)
            cuda_memory_at_start = torch.cuda.memory_allocated(device)

        model.to(device)

        if not self.config.skip_training:
            model.train()
            plugins.on_train_start(self, model)
            plugins.on_train_epoch_start(self, model, epoch_index=0)
            # Measure training forward and backward pass
            for i, batch in enumerate(dataloader):
                batch = plugins.on_train_batch_start(self, model, batch, i)

                inputs, targets = batch
                inputs = self._to_device(inputs, device)
                targets = self._to_device(targets, device)

                if self.config.grad_caching and self.config.sub_batch_size:
                    assert self.config.batch_size % self.config.sub_batch_size == 0, "batch_size must be divisible by sub_batch_size."
                    loss, forward_time, backward_time = self._training_step_with_grad_cache(model, inputs, targets, device, plugins, self.config.sub_batch_size)
                else:
                    logging.info("Gradient caching is disabled")
                    loss, forward_time, backward_time = self._training_step(model, inputs, targets, device, plugins)

                plugins.on_train_batch_end(self, model, loss, batch, i)
                forward_time_all.append(forward_time)
                backward_time_all.append(backward_time)
                if i >= self.config.num_iterations:
                    break

            plugins.on_train_epoch_end(self, model, epoch_index=0)

            if len(forward_time_all) < self.config.num_iterations:
                logger.info(f"The dataset is smaller than expected. The actual number of iteration is {len(forward_time_all)}")

            plugins.on_train_end(self, model)

        if not self.config.skip_prediction:
            model.eval()
            plugins.on_prediction_start(self, model)
            # Measure prediction time.
            for i, batch in enumerate(dataloader):
                batch = plugins.on_prediction_batch_start(self, model, batch, i)
                inputs, targets = batch
                inputs = self._to_device(inputs, device)
                prediction_time_all.append(self._prediction_step(model, inputs, device, plugins))
                if i >= self.config.num_iterations:
                    break

            plugins.on_prediction_end(self, model)

        forward_time_per_iteration = self._mean_without_first_sample(forward_time_all)
        backward_time_per_iteration = self._mean_without_first_sample(backward_time_all)
        forward_backward_time_per_iteration = forward_time_per_iteration + backward_time_per_iteration
        prediction_time_per_iteration = self._mean_without_first_sample(prediction_time_all)
        max_cuda_memory_in_mb = ((torch.cuda.max_memory_allocated(device) - cuda_memory_at_start) / 2 ** 20) if device.type == 'cuda' else 0

        logger.debug(f"{forward_time_all=}")
        logger.debug(f"{backward_time_all=}")
        if prediction_time_all:
            logger.debug(f"{prediction_time_all=}")

        logger.info(f"{forward_time_per_iteration=}, {backward_time_per_iteration=}, {forward_backward_time_per_iteration=}, {prediction_time_per_iteration=}")
        if max_cuda_memory_in_mb > 0:
            logger.info(f"{max_cuda_memory_in_mb=}")

        return self.Outputs(forward_backward_time_per_iteration, forward_time_per_iteration, backward_time_per_iteration, prediction_time_per_iteration, max_cuda_memory_in_mb)

    def _training_step_with_grad_cache(self, model, inputs, targets, device, plugins, sub_batch_size):
        grad_cache_wrapper = BenchmarkGradientCachingTrainer(sub_batch_size)
        return grad_cache_wrapper._training_step(model, inputs, targets, device, plugins)


class BenchmarkGradientCachingTrainer(GradientCachingTrainer):

    def __init__(self, sub_batch_size):
        self._sub_batch_size = sub_batch_size

    def _training_step(self, model, inputs, targets, device, plugins):

        sub_batches = list(zip(self._split_tensor_or_list(inputs), self._split_tensor_or_list(targets)))
        _model = GradientCachingMixin.ModelWrapper(model, device)

        with plugins.forward_context():
            self._synchronize(device)
            start = time.time()
            with torch.no_grad():
                results = [_model(b[0]) for b in sub_batches]
                features_local = [r[0] for r in results]
                rng_states = [r[1] for r in results]
                # Note that a feature vector can contain a scalar tensor. In such case, uses the first scalar value since the trainer assumes all sub_batch returns a same value.
                features = [torch.cat(f, dim=0) if f[0].shape else f[0] for f in zip(*features_local)]

            self._synchronize(device)
            forward_time_first = time.time() - start

        # Set requires_grad in order to calculate gradients for features on this device.
        for f in features:
            f.requires_grad_()

        features_all = [self._all_gather(f) for f in features]
        targets_all = self._all_gather(targets)
        loss = _model.calculate_loss(features_all, targets_all)

        # Run backward pass to calculate gradients for 'features'.
        start = time.time()
        loss = plugins.on_train_backward_start(self, model, loss)
        loss.backward()
        self._synchronize(device)
        plugins.on_train_backward_end(self, model)
        backward_time = time.time() - start

        # Copy the gradients of the feature vectors. Deep-copied so that the subsequent backward pass doesn't affect the cache
        gradient_cache = [self._split_tensor_or_list(copy.deepcopy(f.grad.detach())) for f in features]

        start = time.time()
        for i, sub_batch in enumerate(sub_batches):
            # Run forward pass again, with gradients this time.
            with plugins.forward_context():
                self._synchronize(device)
                features_local_recalculated = _model(sub_batch[0], rng_states[i])[0]
                assert len(features_local_recalculated) == len(gradient_cache)

            maybe_no_sync = self.model.no_sync if hasattr(_model, 'no_sync') and i + 1 != len(sub_batches) else contextlib.nullcontext
            with maybe_no_sync():
                # Run backward pass using the cached gradients for each features.
                for j, f in enumerate(features_local_recalculated):
                    gradient = gradient_cache[j][i] if f.shape else (gradient_cache[j] / len(sub_batches))
                    f.backward(gradient=gradient)

        self._synchronize(device)
        forward_time_second = time.time() - start

        return loss, forward_time_first + forward_time_second, backward_time

    @staticmethod
    def _synchronize(device):
        if device.type == 'cuda':
            torch.cuda.synchronize()
