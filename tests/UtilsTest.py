import os
import json


class UtilsTest(object):
    def __init__(self):
        super().__init__()
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def get_ntl_metric_mock_data(self):
        with open(self.base_path+os.sep+'mock_metric_ntl.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data

    def get_scgc_mock_data(self):
        with open(self.base_path+os.sep+'mock_dataset_scgc.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data

    def get_scgc_metric_mock_data(self):
        with open(self.base_path+os.sep+'mock_metric_scgc.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data
