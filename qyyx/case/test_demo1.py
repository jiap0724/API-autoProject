# -*- coding:utf-8 -*-
# @Time : 2021/2/4 16:01
# @Author : jiapeng
# @File : test_demo1.py
from unittest.test.test_case import Test

import requests
import json
import ddt
import unittest
from ddt import file_data

@ddt.ddt
class testdemo(unittest.TestCase):

    @unittest.skip
    @file_data(r'/Users/jiapeng/Downloads/pythonProject1/qyyx/config/testdata.yaml')
    def test_demo1(self,**testdata):
        name=testdata.get('name')
        password=testdata.get('password')
        print(name)

        print('=====')
        print(password)




    # 封装接口
    def select(self, url, key, city):
        data = {
            "key": key,
            "city": city
        }
        r = requests.post(url, data=data)
        return r

    # 请求数据
    @file_data('city.yaml')
    def test_01(self, value):
        for i in value:
            url = i.get('url')
            key = i.get('key')
            city = i.get('city')
            cake = i.get('cake')
            result = Test().select(url=url, key=key, city=city).text
            self.assertIn(cake, result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
