import unittest
import responses
import os

from datahub_metrics_ingest.ElasticsearchDAO import ElasticsearchDAO


class TestElasticsearchDAO(unittest.TestCase):
    @responses.activate
    def test_writeToElasticsearch_nodata(self):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
            if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'
        responses.add(responses.GET, ELASTICSEARCH_API_BASE_URL + "/metrics/_search?size=10000",
                      json={'hits': {'hits': []}}, status=200)
        test_es_dao = ElasticsearchDAO(elasticsearch_api_base_url=ELASTICSEARCH_API_BASE_URL)
        test_es_dao.write_to_elasticsearch([])
