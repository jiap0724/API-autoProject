# -*- coding:utf-8 -*-
# @Time : 2021/6/1 17:30
# @Author : jiapeng
# @File : test_demo8.py
import logging
import unittest

import jsonpath
import requests
import json
import random
import ddt
from ddt import file_data

from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.requestmethod.HttpRequest import HttpRequest
from axx_unittest.config import getHost
@ddt.ddt()
class axx_learn(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ptpc=None
        cls.ptpcUserId=None
        cls.orderId=None
    #     优化后
        cls.host=getHost.GetHost('../config/host.ini','aixuexi','host')
        cls.ghost = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'ghostrider', 'host')
    # 数据驱动 读取yaml
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_01_login(self,**testdata):
        url=self.host+testdata['path']
        case=testdata['case']
        data=testdata['data']
        r=HttpRequest().http_post(url,None,data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        axx_learn1.ptpc=cookies['ptpc']
        axx_learn1.ptpcUserId=cookies['ptpcUserId']
        self.assertEqual(r.json()['body']['userId'],2720372,msg='登陆失败')
        logging.info('========测试日志信息=========')
        log_case_info(case, url, data, r)


#     订单列表
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_02_pay_list(self,**testdata):
        header=testdata['headers']
        header['ptpc']=self.ptpc
        header['userid']=self.ptpcUserId
        url=self.ghost+testdata['orderlistpath']
        r=HttpRequest().http_get(url,header,None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn1.orderId=jsonpath.jsonpath(r.json(),'$..{0}'.format('orderId'))
        print(axx_learn1.orderId)
        self.assertIsNotNone(axx_learn1.orderId,msg='orderid为空')

#     订单详情

    def test_03_order_detail(self):
        header = {
            'userid': self.ptpcUserId,
            'ptpc': self.ptpc
        }
        orderId=random.choice(self.orderId)
        print(orderId)
        url=self.ghost+'/pop/order/NCTS/pay-order-detail?orderId='+str(orderId)
        r=HttpRequest().http_get(url,header,None)
        # print(r.json())
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # body=jsonpath.jsonpath(r.json(),'$..{0}'.format('goodsName'))
        body=HttpRequest().get_msg(r.text,'body')
        print(str(body))
        self.assertIsNotNone(body,msg='body为空')



if __name__ == '__main__':
    unittest.main(verbosity=2)
