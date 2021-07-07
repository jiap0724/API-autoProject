# -*- coding:utf-8 -*-
# @Time : 2021/6/7 18:22
# @Author : jiapeng
# @File : Login.py
'''
封装用户登陆
'''
import requests
import unittest
import ddt
import yaml

from axx_unittest.config import getHost
from ddt import file_data

from axx_unittest.requestmethod.HttpRequest import HttpRequest


@ddt.ddt()
@classmethod
class GetCookie(unittest.TestCase):

    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def test_login(cls,**testdata):
        host = getHost.GetHost('/Users/jiapeng/Downloads/automationProject/axx_unittest/config/host.ini', 'aixuexi',
                               'host')
        url=host+testdata['path']
        case=testdata['case']
        data=testdata['data']
        r=HttpRequest().http_post(url,None,data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        cls.ptpc=cookies['ptpc']
        cls.ptpcUserId=cookies['ptpcUserId']
        print(cls.ptpcUserId)




