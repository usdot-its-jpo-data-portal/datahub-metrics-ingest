import unittest
import dateutil.parser
from datetime import datetime

from datahub_metrics_ingest.NTLMetricFormatter import NTLMetricFormatter
from UtilsTest import UtilsTest


class TestNTLMetricFormatter(unittest.TestCase):
    def test_getNTLMetricObjects(self):
        test_input = UtilsTest().get_ntl_metric_mock_data()
        test_NTLMetricFormatter = NTLMetricFormatter()
        formatted_output = test_NTLMetricFormatter.get_data_objects(test_input)

        self.assertEqual(len(formatted_output), 5)

    def test_validate_fields(self):
        test_input = UtilsTest().get_ntl_metric_mock_data()
        test_NTLMetricFormatter = NTLMetricFormatter()
        formatted_output = test_NTLMetricFormatter.get_data_objects(test_input)

        in_rec = test_input[0]
        out_rec = formatted_output[0]

        self.assertEqual(type(dateutil.parser.parse(out_rec.timestamp)), datetime, 'Invalid timestamp')
        self.assertEqual(out_rec.granularity, 'monthly', 'Invalid granularity')
        self.assertEqual(out_rec.dh_source_name, 'ntl', 'Invalid dh_source_name')

        self.assertEqual(out_rec.dh_id[:8], 'ntl-dot:', 'Invalid dh_id')
        self.assertEqual(out_rec.user_segment, None, 'Invalid user_segment')
        self.assertEqual(out_rec.access_type, 'page view', 'Invalid access_type')
        self.assertEqual(out_rec.count, int(in_rec['Pageviews']), 'Mismpapped pageviews')