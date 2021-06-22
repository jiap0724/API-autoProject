# -*- coding:utf-8 -*-
# @Time : 2021/6/21 19:27
# @Author : jiapeng
# @File : test_px.py
'''
根据用户选择的标签 推荐课程
'''
import logging
import random
import unittest
import ddt
import jsonpath
import requests
from axx_unittest.Logs.log_info import log_case_info
from axx_unittest.config import getHost
from axx_unittest.requestmethod.HttpRequest import HttpRequest


@ddt.ddt()
class axx_learn(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ptpc=None
        cls.ptpcUserId=None
        cls.courseId=None
        cls.body=None
        cls.labelId=None
    #     优化后
        cls.host=getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini','aixuexi','host')
        cls.pxhost = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'pxhost', 'host')
    # 数据驱动 读取yaml
    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_01_login(self,**testdata):
        url=self.host+testdata['path']
        case=testdata['case']
        data=testdata['data']
        r=HttpRequest().http_post(url,None,data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        axx_learn.ptpc=cookies['ptpc']
        axx_learn.ptpcUserId=cookies['ptpcUserId']
        self.assertEqual(r.json()['body']['userId'],2720372,msg='登陆失败')
        logging.info('========测试日志信息=========')
        log_case_info(case, url, data, r)


#     订单列表
    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_06_getPersonalCourseList(self, **testdata):
        header = testdata['headers']
        header['ptpc'] = self.ptpc
        header['userid'] = self.ptpcUserId
        url = self.pxhost + testdata['CourseListpath']
        r = HttpRequest().http_get(url, header, None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn.courseId = jsonpath.jsonpath(r.json(), '$..{0}'.format('id'))
        print(axx_learn.courseId)
        self.assertIsNotNone(axx_learn.courseId, msg='orderid为空')

    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_03_labelList(self, **testdata):
        header = testdata['headers']
        header['ptpc'] = self.ptpc
        header['userid'] = self.ptpcUserId
        url = self.pxhost + testdata['labelListpath']
        r = HttpRequest().http_get(url, header, None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn.labelId = jsonpath.jsonpath(r.json(), '$..{0}'.format('labelId'))
        self.assertIsNotNone(axx_learn.labelId, msg='labelId为空')

    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_04_userInterestLabel(self, **testdata):
        header = testdata['headers']
        header['ptpc'] = self.ptpc
        header['userid'] = self.ptpcUserId
        url = self.pxhost + testdata['userInterestLabelpath']
        r = HttpRequest().http_get(url, header, None)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn.body = jsonpath.jsonpath(r.json(), '$..{0}'.format('body'))
        self.assertIsNotNone(axx_learn.body, msg='body为空')

    @ddt.file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_05_saveUserInterestLabel(self, **testdata):
        header = testdata['headers']
        header['ptpc'] = self.ptpc
        header['userid'] = self.ptpcUserId
        labId=random.choices(self.labelId,k=2)
        data=[
            {'labelId':str(labId[0])},
            {'labelId':str(labId[1])}
        ]
        url = self.pxhost + testdata['saveUserInterestLabelpath']
        r = HttpRequest().http_post(url, header, data)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        # key = input('请输入要获取的key:')
        axx_learn.body = jsonpath.jsonpath(r.json(), '$..{0}'.format('body'))
        print(axx_learn.body)
        # self.assertIsNotNone(axx_learn.body, msg='body为空')
        self.assertEqual(axx_learn.body,['保存成功'],msg='保存失败')


if __name__ == '__main__':
    unittest.main(verbosity=2)
