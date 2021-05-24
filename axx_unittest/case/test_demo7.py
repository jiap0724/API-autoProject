# -*- coding:utf-8 -*-
# @Time : 2021/5/24 15:04
# @Author : jiapeng
# @File : test_demo7.py
import json
import unittest

import requests

from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.Logs.demolog import *
from axx_unittest.requestmethod.HttpRequest import HttpRequest
import ddt #数据驱动
from ddt import unpack,data,file_data

@ddt.ddt()
class axx_learn(unittest.TestCase):
    def setUp(self) -> None:
        self.host='https://admin.aixuexi.com/shooter/manage/passwordLogin'
        print('初始化')

    def tearDown(self) -> None:
        print('tearDown')

    # 读取yaml
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata1.yaml')
    def test_login1(self,data,case,msg):
        print(case)
        r = HttpRequest().http_request(self.host,data,'post',None,None)
        print(r)
        self.assertEqual(msg,r['errorMessage'])
        logging.info('========测试日志信息=========')
        log_case_info(case, self.host, data, r)

if __name__ == '__main__':
    unittest.main(verbosity=2)
