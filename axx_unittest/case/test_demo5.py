# -*- coding:utf-8 -*-
# @Time : 2021/5/18 15:41
# @Author : jiapeng
# @File : test_demo5.py
import unittest
import requests
import json
import ddt #数据驱动
from ddt import unpack,data,file_data

from axx_unittest.HTMLTestReportCN import HTMLTestRunner


@ddt.ddt()
class axx_learn(unittest.TestCase):
    def setUp(self) -> None:
        self.host='https://admin.aixuexi.com/shooter/manage/passwordLogin'
        print('初始化')

    def tearDown(self) -> None:
        print('tearDown')

    # 多个元素还需要使用unpack
    @data(['jiapeng0@aixuexi.com','Jiapeng0724'],['jiapeng0@aixuexi.com','Jiapeng0724'],['jiapeng0@aixuexi.com','Jiapeng0724'])
    @unpack
    def test_login(self,username,password):
        data = {
            'username': username,
            'password': password
        }
        r = requests.post(url=self.host, data=data)
        # print(r.cookies)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    # 读取yaml
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata.yaml')
    def test_login1(self,**testdata):
        casename = testdata.get('case')
        print(casename)

        data = {
            'username': testdata.get('username'),
            'password': testdata.get('password')
        }

        r = requests.post(url=self.host, data=data)
        # print(r.cookies)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main(verbosity=2)

