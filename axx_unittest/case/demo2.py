# -*- coding:utf-8 -*-
# @Time : 2021/5/18 14:29
# @Author : jiapeng
# @File : demo2.py
import unittest
import requests
import json
class axx_learn2(unittest.TestCase):
    def test_login(self):
        url = 'https://admin.aixuexi.com/shooter/manage/passwordLogin'
        data = {
            'username': 'jiapeng0@aixuexi.com',
            'password': 'Jiapeng0724'
        }
        r = requests.post(url, data)
        # print(r.cookies)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))

    def test_login1(self):
        url = 'https://admin.aixuexi.com/shooter/manage/passwordLogin'
        data = {
            'username': 'jiapeng0@aixuexi.com',
            'password': 'Jiapeng0724'
        }
        r = requests.post(url, data)
        # print(r.cookies)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        status=r.json()['status']
        userId=r.json()['body']['userId']
        self.assertEquals(status,1)
        self.assertEquals(userId, 2716742)

if __name__ == '__main__':
    unittest.main(verbosity=2)
