#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-19 17:02:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import unittest
from dataCollector import typhoonCollector
from dataCollector.apis import server


class API_TEST(unittest.TestCase):
    """docstring for API_TEST"""

    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        print('Test done')

    def test_Typhoon(self):
        rv = self.app.get('/apis/typhoon/2016')
        assert rv.status_code == 200

    def test_Typhoon_info(self):
        rv = self.app.get('/apis/typhooninfo/2308229')
        assert rv.status_code == 200

    def test_Typhoon_years(self):
        rv = self.app.get('/apis/typhooninfo/years')
        assert rv.status_code == 200

    def test_Typhoon_loc(self):
        rv = self.app.get('/apis/typhoonloc/2308229')
        assert rv.status_code == 200


if __name__ == '__main__':
    typhoonCollector.col.drop()
    for x in xrange(2015, 2017):
        typhoonCollector.get_typhoon_data(x)
    year_info = typhoonCollector.col.find({}, {'typhoonid': 1, '_id': 0})
    for typhoonid in year_info:
        typhoonCollector.get_typhoon_info(typhoonid['typhoonid'])

    unittest.main()
