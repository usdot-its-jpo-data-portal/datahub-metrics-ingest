from datahub_metrics_ingest.SocrataMetricFormatter import SocrataMetricFormatter
from datahub_metrics_ingest.NTLMetricFormatter import NTLMetricFormatter

TYPE_NTL = 'ntl'
TYPE_SOCRATA = 'socrata'


class FormatterFactory(object):
    def __init__(self):
        super().__init__()

    def get_formatter(self, data_type):
        switcher = {
            TYPE_NTL: NTLMetricFormatter(),
            TYPE_SOCRATA: SocrataMetricFormatter()
        }

        return switcher.get(data_type, None)
