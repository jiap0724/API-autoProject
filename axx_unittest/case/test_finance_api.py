# -*- coding:utf-8 -*-
# @Time : 2021/6/9 10:59
# @Author : jiapeng
# @File : test_finance_api.py
'''
财务接口
'''
import unittest
import jsonpath
import yaml

from axx_unittest.config import getHost
from axx_unittest.requestmethod.HttpRequest import HttpRequest
import ddt
@ddt.ddt()
class Finance(unittest.TestCase):


    def setUp(self) -> None:

        self.host = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'ghostrider',
                                   'host')

    # 数据驱动 读取yaml
    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_01_login(self, **testdata):
        header = {

        }
        url=self.ghost+testdata['orderlistpath']
        r=HttpRequest().http_get(url,header,None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        Finance.orderId=jsonpath.jsonpath(r.json(),'$..{0}'.format('orderId'))
        print(Finance.orderId)
        self.assertIsNotNone(Finance.orderId,msg='orderid为空')


