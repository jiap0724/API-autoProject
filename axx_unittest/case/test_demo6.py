# -*- coding:utf-8 -*-
# @Time : 2021/5/18 15:41
# @Author : jiapeng
# @File : test_demo6.py
import unittest
import requests
import json
import ddt #数据驱动
from ddt import unpack,data,file_data

from axx_unittest.HTMLTestReportCN import HTMLTestRunner
from axx_unittest.requestmethod.HttpRequest import HttpRequest


@ddt.ddt()
class axx_learn(unittest.TestCase):
    def setUp(self) -> None:
        self.host='https://admin.aixuexi.com/shooter/manage/passwordLogin'
        print('初始化')

    def tearDown(self) -> None:
        print('tearDown')

    # 读取yaml
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata.yaml')
    def test_login1(self,**testdata):
        casename = testdata.get('case')
        print(casename)

        data = {
            'username': testdata.get('username'),
            'password': testdata.get('password')
        }

        r = HttpRequest().http_request(self.host, data, 'post', None, None)

        print(r)

if __name__ == '__main__':
    unittest.main(verbosity=2)
