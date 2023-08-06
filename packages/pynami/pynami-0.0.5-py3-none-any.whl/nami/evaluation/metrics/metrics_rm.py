from collections import defaultdict

from franky.evaluator import BaseMetric
from nami.registry import METRICS


@METRICS.register_module()
class RMMetrics(BaseMetric):
    def process(self, data_batch, data_samples):
        """Process one batch of data samples.

        The processed results should be stored in ``self.results``, which will
        be used to computed the metrics when all batches have been processed.

        Args:
            data_batch: A batch of data from the dataloader.
            data_samples (Sequence[dict]): A batch of outputs from the model.
        """
        results = defaultdict(list)
        for sample_idx, pred_label in zip(data_batch['sample_idx'], data_samples[0]):
            results[sample_idx].append(pred_label)
        for idx, pred in results.items():
            self.results.append(dict(idx=idx, pred=pred))

    def compute_metrics(self, results):
        """Compute the metrics from processed results.

        Args:
            results (dict): The processed results of each batch.

        Returns:
            Dict: The computed metrics. The keys are the names of the metrics,
            and the values are corresponding results.
        """
        # NOTICE: don't access `self.results` from the method.
        correct = 0
        for result in results:
            pred = result['pred']
            if pred == sorted(pred, reverse=True):
                correct += 1
        metrics = dict(acc=correct / len(results))
        return metrics
