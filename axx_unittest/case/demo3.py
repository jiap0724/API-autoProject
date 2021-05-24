# -*- coding:utf-8 -*-
# @Time : 2021/5/18 15:36
# @Author : jiapeng
# @File : demo3.py
import unittest
import requests
import json

class axx_learn(unittest.TestCase):
    def setUp(self) -> None:
        self.host='https://admin.aixuexi.com/shooter/manage/passwordLogin'

    def tearDown(self) -> None:
        print('tearDown')

    def test_login(self):
        data = {
            'username': 'jiapeng0@aixuexi.com',
            'password': 'Jiapeng0724'
        }
        r = requests.post(url=self.host, data=data)
        # print(r.cookies)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        print(r.text)

    def test_login1(self):
        data = {
            'username': 'jiapeng0@aixuexi.com',
            'password': 'Jiapeng0724'
        }
        r = requests.post(url=self.host, data=data)
        # print(r.cookies)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main(verbosity=2)
