# -*- coding:utf-8 -*-
# @Time : 2021/6/1 17:30
# @Author : jiapeng
# @File : demo7.py
import unittest

import jsonpath
import requests
import json
import random

from axx_unittest.requestmethod.HttpRequest import HttpRequest
from axx_unittest.config import getHost

class axx_learn(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ptpc=None
        cls.ptpcUserId=None
        cls.orderId=None
    #     优化后
        cls.host=getHost.GetHost('../config/host.ini','aixuexi','host')
        cls.ghost = getHost.GetHost('../config/host.ini', 'ghostrider', 'host')

    def test_01_login(self):
        url=self.host+'/surrogates/passport/user/v2/login'
        data={
            "device": "6619a89f4edf3cf778b5bf335a02458f",
            "loginType": 1,
            "password": "qa123456",
            "username": "15210060668",
            "validateCode": "",
            "loginSystem": "pc"
        }

        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        r=HttpRequest().http_post(url,None,data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        axx_learn.ptpc=cookies['ptpc']
        axx_learn.ptpcUserId=cookies['ptpcUserId']
        self.assertEqual(r.json()['body']['userId'],2720372,msg='登陆失败')


#     订单列表
    def test_02_pay_list(self):
        header={
            'userid':self.ptpcUserId,
            'ptpc':self.ptpc
        }
        url=self.ghost+'/pop/order/pay-list?studentName=&orderNo=&phone=&goodsName=&orderStatus=&businessType=1&orderSource=&orderAccount=&pageNum=1&pageSize=10&startTime=2021-05-03%2000:00:00&endTime=2021-06-02%2023:59:59'
        r=HttpRequest().http_get(url,header,None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn.orderId=jsonpath.jsonpath(r.json(),'$..{0}'.format('orderId'))
        print(axx_learn.orderId)
        self.assertIsNotNone(axx_learn.orderId,msg='orderid为空')

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
    unittest.main()
