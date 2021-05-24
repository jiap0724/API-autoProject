# -*- coding:utf-8 -*-
# @Time : 2021/5/6 19:12
# @Author : jiapeng
# @File : QuerySms.py
import requests
import json
import unittest

class Axx_QuerySms(unittest.TestCase):
    def test_queryResult(self):
        url='https://zjj-public.ghost.aixuexi.com/sms/queryRecordResult?taskId=SMS-SMS_215510238-20210506175731-VVqYfP&offsetId=0'
        headers={'X-Access-Token': 'J7G7iuHM:1634981511:5a11117961da3d72516db0452c4c6259'}
        r=requests.get(url=url,headers=headers)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))
