# -*- coding:utf-8 -*-
# @Time : 2021/6/25 11:51
# @Author : jiapeng
# @File : test_px_demo.py
import logging
import random
import unittest
import ddt
import jsonpath
import requests

from axx_unittest.GetCookie import GetHeader
from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.config import getHost
from axx_unittest.requestmethod.HttpRequest import HttpRequest


@ddt.ddt()
class axx_learn(unittest.TestCase):
    def setUp(self) -> None:
        self.headers=GetHeader().test_Getheaders()
        self.courseId = None
        self.body = None
        self.labelId = None
        #     优化后
        self.host = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'aixuexi',
                                   'host')
        self.pxhost = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini',
                                     'pxhost', 'host')

    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_01_labelList(self, **testdata):
        header=self.headers
        url = self.pxhost + testdata['labelListpath']
        r = HttpRequest().http_get(url, header, None)
        axx_learn.labelId = jsonpath.jsonpath(r.json(), '$..{0}'.format('labelId'))
        self.assertIsNotNone(axx_learn.labelId, msg='labelId为空')

if __name__ == '__main__':
    unittest.main(verbosity=2)
