import csv

from datahub_metrics_ingest.DHMetric import DHMetric


def write_metrics_to_csv(fp: str, metric_objs: [DHMetric]):
    headers = "timestamp,granularity,dh_id,dh_source_name,user_segment,access_type,count".split(',')
    with open(fp, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for m in metric_objs:
            writer.writerow([
                m.timestamp, m.granularity, m.dh_id, m.dh_source_name,
                m.user_segment, m.access_type, m.count])