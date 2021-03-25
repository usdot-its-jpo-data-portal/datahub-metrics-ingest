import unittest
import dateutil.parser
from datetime import datetime
import re

from datahub_metrics_ingest.SocrataMetricFormatter import SocrataMetricFormatter
from UtilsTest import UtilsTest


class TestSocrataMetricFormatter(unittest.TestCase):
    def test_getSocrataMetricObjects(self):
        test_results = UtilsTest().get_scgc_metric_mock_data()
        test_socrata_metric_formatter = SocrataMetricFormatter()
        formatted_results = test_socrata_metric_formatter.get_data_objects(test_results, 'scgc')

        self.assertEqual(len(formatted_results), 6, 'Metrics not aggregated properly')
        self.assertEqual(
            sum([int(i['value']) for i in test_results]), 
            sum([i.count for i in formatted_results]),
            'Sum of aggregated metric values do not equal to sum of source metric values'
        )

    def test_validate_fields_dtg(self):
        test_input = UtilsTest().get_scgc_metric_mock_data()
        test_socrata_metric_formatter = SocrataMetricFormatter()
        formatted_results = test_socrata_metric_formatter.get_data_objects(test_input[:1], 'scgc')
        out_rec = formatted_results[0]

        self.assertEqual(type(dateutil.parser.parse(out_rec.timestamp)), datetime, 'Invalid timestamp')
        self.assertEqual(out_rec.granularity, 'daily', 'Invalid granularity')
        self.assertEqual(out_rec.dh_source_name, 'scgc', 'Invalid dh_source_name')

        self.assertTrue(re.match(r'scgc-[a-z0-9]{4}-[a-z0-9]{4}', out_rec.dh_id), 'Invalid dh_id')
        self.assertIsNot(out_rec.user_segment, None, 'Invalid user_segment')
        self.assertIsNot(out_rec.access_type, None, 'Invalid access_type')

        formatted_results_dtg = test_socrata_metric_formatter.get_data_objects(test_input[1:], 'dtg')
        out_rec_dtg = formatted_results_dtg[0]

        self.assertEqual(out_rec_dtg.dh_source_name, 'dtg', 'Invalid dh_source_name')