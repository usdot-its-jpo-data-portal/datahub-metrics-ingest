import unittest

from datahub_metrics_ingest.FormatterFactory import FormatterFactory
from datahub_metrics_ingest.NTLMetricFormatter import NTLMetricFormatter
from datahub_metrics_ingest.SocrataMetricFormatter import SocrataMetricFormatter


class TestFormatterFactory(unittest.TestCase):
    def test_get_formatter_ntl(self):
        formatter = FormatterFactory().get_formatter('ntl')
        self.assertTrue(isinstance(formatter, NTLMetricFormatter))

    def test_get_formatter_socrata(self):
        formatter = FormatterFactory().get_formatter('socrata')
        self.assertTrue(isinstance(formatter, SocrataMetricFormatter))

    def test_get_formatter_invalid(self):
        formatter = FormatterFactory().get_formatter('a formater that does not exists')
        self.assertIsNone(formatter)
