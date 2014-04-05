# -*- coding: utf-8 -*-
import unittest


from mysolr import SolrResponse
from os.path import join, dirname
import requests
import json
import sys

class HighlightingQueryResultTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        mock_file = join(dirname(__file__), 'mocks/highlightingquery')
        with open(mock_file) as f:
            raw_content = None
            if sys.version_info[0] == 3:
                raw_content = f.read().encode('utf-8')
            else:
                raw_content = f.read()
            self.response = SolrResponse()
            self.response.raw_content = raw_content
            self.response.status = 200
            self.response.parse_content()

    def tearDown(self):
        pass

    def test_query(self):
        self.assertNotEqual(self.response.highlighting, None)


if __name__ == '__main__':
    unittest.main()