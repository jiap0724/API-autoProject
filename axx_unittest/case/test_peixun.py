# -*- coding:utf-8 -*-
# @Time : 2021/6/11 11:56
# @Author : jiapeng
# @File : test_peixun.py
import logging
import jsonpath
import requests
import unittest
import ddt
import yaml
from ddt import file_data
from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.config import getHost
from axx_unittest.requestmethod.HttpRequest import HttpRequest

class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ptpc = None
        cls.ptpcUserId = None
        cls.id = None
        #     优化后
        cls.host = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'aixuexi',
                                   'host')
        cls.pxhost = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini',
                                    'pxhost', 'host')

    # 数据驱动 读取yaml
    @unittest.skip
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_01_login(self, **testdata):
        url = self.host + testdata['path']
        case = testdata['case']
        data = testdata['data']
        r = HttpRequest().http_post(url, None, data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        demo.ptpc = cookies['ptpc']
        demo.ptpcUserId = cookies['ptpcUserId']
        self.assertEqual(r.json()['body']['userId'], 2720372, msg='登陆失败')
        logging.info('========测试日志信息=========')
        log_case_info(case, url, data, r)

    @unittest.skip
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_02_getPersonalCourseList(self,**testdata):
        header = testdata['headers']
        header['ptpc'] = self.ptpc
        header['userid'] = self.ptpcUserId
        url = self.pxhost + testdata['CourseListpath']
        r = HttpRequest().http_get(url, header, None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        demo.id = jsonpath.jsonpath(r.json(), '$..{0}'.format('id'))
        print(demo.orderId)
        self.assertIsNotNone(demo.id, msg='orderid为空')


    def test_demo(self):
        with open('/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata3.yaml') as f:
            temp=yaml.load(f.read(),Loader=yaml.FullLoader)
        for key, values in temp.items():
            print(key,":",values)


if __name__ == '__main__':
    unittest.main(verbosity=2)
