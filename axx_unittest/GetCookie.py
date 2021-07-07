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
import unittest
# @ddt.ddt()
class GetHeader(unittest.TestCase):
    # @classmethod
    # @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/LoginData.yaml')
    # def Getptpc(cls,**testdata):
    #     url='http://www.aixuexi.com/surrogates/passport/user/v2/login'
    #     data=testdata['data']
    #     r=requests.post(url,json=data)
    #     # 把返回的cookie转换为字典
    #     cookies = requests.utils.dict_from_cookiejar(r.cookies)
    #     cls.ptpc = cookies['ptpc']
    #     cls.ptpcUserId = cookies['ptpcUserId']
    #     print(cls.ptpc)
    #     return cls.ptpc
    #
    # @classmethod
    # @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/LoginData.yaml')
    # def Getuserid(cls, **testdata):
    #     url = 'http://www.aixuexi.com/surrogates/passport/user/v2/login'
    #     data = testdata.get('data')
    #     r = requests.post(url,json=data)
    #     # 把返回的cookie转换为字典
    #     cookies = requests.utils.dict_from_cookiejar(r.cookies)
    #     cls.ptpc = cookies['ptpc']
    #     cls.ptpcUserId = cookies['ptpcUserId']
    #     # yamlpath = '/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/testdata3.yaml'
    #     # headers = {
    #     #     'ptpc': cls.ptpc,
    #     #     'userid': cls.ptpcUserId
    #     # }
    #     # with open(yamlpath, "w", encoding="utf-8") as f:
    #     #     yaml.dump(headers, f,Dumper=yaml.RoundTripDumper)
    #     return cls.ptpcUserId

    # @classmethod
    # @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/LoginData.yaml')
    # def test_GetHeader(self, **testdata):
    #     url = 'http://www.aixuexi.com/surrogates/passport/user/v2/login'
    #     data=testdata['data']
    #     r = requests.post(url, json=data)
    #     # 把返回的cookie转换为字典
    #     cookies = requests.utils.dict_from_cookiejar(r.cookies)
    #     ptpc = cookies['ptpc']
    #     ptpcUserId=cookies['ptpcUserId']
    #     self.headers = {
    #                 'ptpc': ptpc,
    #                 'userid': ptpcUserId
    #             }
    #     print(type(self.headers))
    #     return self.headers

    # @classmethod
    # def Getuserid(self):
    #     url = 'http://www.aixuexi.com/surrogates/passport/user/v2/login'
    #     data = {
    #         'device': 'dffb64a4b76134eae61aab58c541bd33',
    #         'loginType': '1',
    #         'password': 'qa123456',
    #         'username': '15210060668',
    #         'validateCode': '',
    #         'loginSystem': 'pc'
    #     }
    #     r = requests.post(url, json=data)
    #     # 把返回的cookie转换为字典
    #     cookies = requests.utils.dict_from_cookiejar(r.cookies)
    #     self.ptpcUserId = cookies['ptpcUserId']
    #     return self.ptpcUserId

    # @file_data(r'/Users/jiapeng/Downloads/automationProject/axx_unittest/TestData/LoginData.yaml')
    # def test_yaml(self,**testdata):
    #     data1=testdata['data']
    #     print(data1)

    def test_Getheaders(self):
        url = 'http://www.aixuexi.com/surrogates/passport/user/v2/login'
        data = {
            'device': 'dffb64a4b76134eae61aab58c541bd33',
            'loginType': '1',
            'password': 'qa123456',
            'username': '15210060668',
            'validateCode': '',
            'loginSystem': 'pc'
        }
        r = requests.post(url, json=data)
        # 把返回的cookie转换为字典
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        ptpc = cookies['ptpc']
        ptpcUserId=cookies['ptpcUserId']
        self.headers = {
                    'ptpc': ptpc,
                    'userid': ptpcUserId
                }
        print(self.headers)
        return self.headers


#
# if __name__ == '__main__':
#     unittest.main()
