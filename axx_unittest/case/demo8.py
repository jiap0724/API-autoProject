# -*- coding:utf-8 -*-
# @Time : 2021/6/5 18:10
# @Author : jiapeng
# @File : demo8.py
import unittest
import requests
import ddt
from ddt import file_data
@ddt.ddt()
class demo8(unittest.TestCase):
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_login(self,**testdata):
        url=testdata['url']
        print(url)
        data=testdata['data']
        print(type(data))
        r=requests.post(url,json=data)
        print(r.json())

