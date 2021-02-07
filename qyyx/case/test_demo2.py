# -*- coding:utf-8 -*-
# @Time : 2021/2/4 17:15
# @Author : jiapeng
# @File : test_demo2.py
import unittest
import requests
import ddt
from ddt import unpack,data,file_data
import json
from qyyx.Logs.log_info import log_case_info
from qyyx.Logs.demolog import *

@ddt.ddt
class testdemo2(unittest.TestCase):

    def setUp(self):
        self.host='http://apis.juhe.cn/simpleWeather/query'

    # 这是数据分离格式的

    @data(['331eab8f3481f37868378fcdc76cb7cd','北京'])
    @unpack
    def testcase01(self,key,city):
        data={
            'key':key,
            'city':city
        }
        r=requests.post(url=self.host,data=data)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))


#     这是读取yaml的
    @file_data(r'/Users/jiapeng/Downloads/pythonProject1/qyyx/config/testdata.yaml')
    def testcase02(self,**testdata):
        casename = testdata.get('case')
        print(casename)

        data = {
            'key': testdata.get('key'),
            'city': testdata.get('city')
        }
        r = requests.post(url=self.host, data=data)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        log_case_info(casename,self.host,data,r.text)
        logging.info('这是测试用例2')




if __name__ == '__main__':
    unittest.main(verbosity=2)

