import csv
import io
from typing import List, Dict
from datahub_metrics_ingest.DHMetric import DHMetric


def read_csv(infile: io.TextIOWrapper) -> List[Dict[str, str]]:
    recs = []
    str_line = lambda line: line.decode('utf-8') if type(line) == bytes else line
    process_line = lambda line: [i.strip() for i in str_line(line).split(',')]
    
    line = infile.readline()
    headers = process_line(line)

    line = infile.readline()
    while line:
        row = dict(zip(headers, process_line(line)))
        recs.append(row)
        line = infile.readline()
    return recs

def write_metrics_to_csv(fp: str, metric_objs: [DHMetric]):
    headers = "timestamp,granularity,dh_id,dh_source_name,user_segment,access_type,count".split(',')
    with open(fp, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for m in metric_objs:
            writer.writerow([
                m.timestamp, m.granularity, m.dh_id, m.dh_source_name,
                m.user_segment, m.access_type, m.count])
