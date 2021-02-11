import dateutil.parser

from datahub_metrics_ingest.DHMetric import DHMetric
from datahub_metrics_ingest.FormatterInterface import FormatterInterface


class NTLMetricFormatter(FormatterInterface):
    def __init__(self):
        pass    #intentionally empty constructor

    def get_data_objects(self, metrics) -> [DHMetric]:

        result = []

        for metric in metrics:
            if metric is None:
                continue

            dm = DHMetric()
            dm.timestamp = dateutil.parser.parse(metric['Month']).strftime('%Y-%m-01')
            dm.granularity = 'monthly'
            dm.dh_source_name = 'ntl'
            dm.dh_id = f"{dm.dh_source_name}-dot:{metric['Page'].split('/')[-1]}"
            dm.user_segment = None
            dm.access_type = 'page view'
            dm.count = int(metric['Pageviews'])

            result.append(dm)

        return result
