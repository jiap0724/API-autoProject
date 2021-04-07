# -*- coding:utf-8 -*-
# @Time : 2021/4/7 16:17
# @Author : jiapeng
# @File : demo2.py
import unittest
import json
import requests
from qyyx.case.demo1 import Login
class demo2(unittest.TestCase):
    def test_xiaoqu(self):
        url = "https://oms.admin.aixuexi.com/marketingcenter/marketingactivity//institutions"
        r = requests.get(url, cookies=Login.test_login())
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main(verbosity=2)
