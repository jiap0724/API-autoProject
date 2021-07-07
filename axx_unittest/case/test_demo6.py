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
from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.Logs.demolog import *
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

        r=HttpRequest().http_post_data(self.host,None,data)
        print(r)
        logging.info('========测试日志信息=========')
        log_case_info(casename, self.host, data, r)

if __name__ == '__main__':
    unittest.main(verbosity=2)

