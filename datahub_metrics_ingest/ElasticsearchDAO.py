import os
import requests
import json


class ElasticsearchDAO(object):
    def __init__(self):
        super().__init__()

    def write_to_elasticsearch(self, metrics):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
                                     if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'
        document = ''
        for metric in metrics:
            line_obj = {}
            line_index_obj = {}

            line_obj = self.map_obj_doc(metric, {})
            line_index_obj['index'] = {'_id': self.format_es_id(metric), '_index': 'metrics'}

            document += json.dumps(line_index_obj) + '\r\n'
            document += json.dumps(line_obj) + '\r\n'

        if document != '':
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(f'{ELASTICSEARCH_API_BASE_URL}/_bulk', data=document, headers=header)
            print(f'Data written to ES: {es_post_response.status_code} {es_post_response.reason} ({len(metrics)})')

    def map_obj_doc(self, metric, line_obj_doc):
        new_lineobj_doc = {}

        new_lineobj_doc['timestamp'] = metric.timestamp
        new_lineobj_doc['granularity'] = metric.granularity
        new_lineobj_doc['dhId'] = metric.dh_id
        new_lineobj_doc['dhSourceName'] = metric.dh_source_name
        new_lineobj_doc['userSegment'] = metric.user_segmnet
        new_lineobj_doc['accessType'] = metric.access_type
        new_lineobj_doc['count'] = metric.count
        
        return new_lineobj_doc
    
    def format_es_id(self, m):
        es_id = f'{m.dh_id}::{m.timestamp}::{m.granularity}::{m.access_type}::{m.user_segment}'
        return es_id