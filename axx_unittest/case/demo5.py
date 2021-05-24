# -*- coding:utf-8 -*-
# @Time : 2021/5/24 10:34
# @Author : jiapeng
# @File : demo5.py

import unittest
import ddt #数据驱动
from ddt import unpack,data,file_data
from axx_unittest.requestmethod.HttpRequest import HttpRequest

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
    def test_login001(self,username,password):
        data = {
            'username': username,
            'password': password
        }

        res=HttpRequest().http_request(self.host,data,'post',None,None)
        print(res)


    # 读取yaml
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata.yaml')
    def test_login002(self,**testdata):
        casename = testdata.get('case')
        print(casename)
        data = {
            'username': testdata.get('username'),
            'password': testdata.get('password')
        }
        res=HttpRequest().http_request(self.host,data,'post',None,None)
        print(res)

if __name__ == '__main__':
    unittest.main(verbosity=2)
