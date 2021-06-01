# -*- coding:utf-8 -*-
# @Time : 2021/6/1 17:30
# @Author : jiapeng
# @File : demo7.py
import unittest
import requests
import json

class axx_learn(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ptpc=None
        cls.ptpcUserId=None

    def test_login(self):
        url='http://www.aixuexi.com/surrogates/passport/user/v2/login'
        data={
            "device": "23582a6aa449a38775e7f05b7941f97c",
            "loginType": 1,
            "password": "qa123456",
            "username": "15210060668",
            "validateCode": "",
            "loginSystem": "pc"
        }
        r=requests.post(url=url,json=data)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))

        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        axx_learn.ptpc=cookies['ptpc']
        axx_learn.ptpcUserId=cookies['ptpcUserId']


#     订单列表
    def test_pay_list(self):
        header={
            'userid':self.ptpcUserId,
            'ptpc':self.ptpc
        }
        url='http://ghostrider.aixuexi.com/pop/order/pay-list?studentName=&orderNo=&phone=&goodsName=&orderStatus=&businessType=1&orderSource=&orderAccount=&pageNum=1&pageSize=10&startTime=2021-05-03%2000:00:00&endTime=2021-06-02%2023:59:59'
        r=requests.get(url=url,headers=header)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()
