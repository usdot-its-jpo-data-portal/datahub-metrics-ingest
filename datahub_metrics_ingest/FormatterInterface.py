from abc import ABC, abstractmethod
from datahub_metrics_ingest.DHMetric import DHMetric


class FormatterInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_data_objects(self, metric, source_name) -> [DHMetric]:
        raise NotImplementedError
