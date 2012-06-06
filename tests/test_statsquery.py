# -*- coding: utf-8 -*-
import unittest


from mysolr import SolrResponse
from os.path import join, dirname
import requests
import sys
import json


class StatsQueryTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        mock_file = join(dirname(__file__), 'mocks/statsquery')
        with open(mock_file) as f:
            raw_content = None
            if sys.version_info.major == 3 and sys.version_info.minor == 2:
                raw_content = json.dumps(eval(f.read())).encode('utf-8')
            else:
                raw_content = f.read()
            self.response = SolrResponse()
            self.response.raw_content = raw_content
            self.response.status = 200
            self.response.parse_content()
    def tearDown(self):
        pass

    def test_query(self):
        self.assertNotEqual(self.response.stats, None)


if __name__ == '__main__':
    unittest.main()