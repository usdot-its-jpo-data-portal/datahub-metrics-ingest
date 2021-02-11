from datahub_metrics_ingest.DHMetric import DHMetric
from datahub_metrics_ingest.FormatterInterface import FormatterInterface


class SocrataMetricFormatter(FormatterInterface):

    def __init__(self):
        pass  #intentionally empty constructor

    def get_data_objects(self, metrics) -> [DHMetric]:
        # aggregate hourly metric to daily metric
        daily_metric_dict = {}
        for m in metrics:
            key = m['timestamp'][:10], m['asset_uid'], m['user_segment'], m['access_type']
            if key in daily_metric_dict:
                daily_metric_dict[key] += int(m['value'])
            else:
                daily_metric_dict[key] = int(m['value'])
        
        # map to DHMetric objects
        result = []        
        for m_meta, count in daily_metric_dict.items():
            date, asset_uid, user_segment, access_type = m_meta

            dm = DHMetric()
            dm.timestamp = date
            dm.granularity = 'daily'
            dm.dh_source_name = 'scgc'
            dm.dh_id = f'{dm.dh_source_name}-{asset_uid}'
            dm.user_segment = user_segment
            dm.access_type = access_type
            dm.count = count
            result.append(dm)

        return result
