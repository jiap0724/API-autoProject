# -*- coding:utf-8 -*-
# @Time : 2021/6/21 16:02
# @Author : jiapeng
# @File : GetCookie.py
'''
登陆获取cookie
'''

import requests
import ddt
from ddt import file_data
from ruamel import yaml

@ddt.ddt()
class GetCookie():
    @classmethod
    @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata2.yaml')
    def GetUserCookie(cls,**testdata):
        url='http://www.aixuexi.com/surrogates/passport/user/v2/login'
        data=testdata['data']
        r=requests.post(url,data)
        # 把返回的cookie转换为字典
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        cls.ptpc = cookies['ptpc']
        cls.ptpcUserId = cookies['ptpcUserId']
        yamlpath = '/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata3.yaml'
        headers = {
            'ptpc': cls.ptpc,
            'userid': cls.ptpcUserId
        }
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(headers, f,Dumper=yaml.RoundTripDumper)

