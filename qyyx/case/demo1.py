# -*- coding:utf-8 -*-
# @Time : 2021/3/31 14:02
# @Author : jiapeng
# @File : demo1.py
# import random
# list=[2,3,4,5,6,10,21,19]
# id_num =random.choice(list)
# print(id_num)
# print(type(id_num))
'''
获取登陆cookie
'''
import requests
import json
import unittest
import random

class Login(unittest.TestCase):
    global cookies
    def test_login(self):
        url='https://admin.aixuexi.com/shooter/manage/passwordLogin'
        data={
            'username':'jiapeng0@aixuexi.com',
            'password':'Jiapeng0724'
        }
        r=requests.post(url,data)
        # print(r.cookies)
        # print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        cookies1 = r.cookies.items()

        cookie = ''
        for name, value in cookies1:
            cookie += '{0}={1};'.format(name, value)

        print(cookie)
        # print(cookies)
        globals()['cookies']=r.cookies

    @unittest.skip
    #校区列表
    def test_xiaoqu(self):
        url = "http://oms.admin.aixuexi.com/marketingcenter/marketingactivity/institutions?pageNum=1&pageSize=10"
        r = requests.get(url, cookies=cookies,verify=False)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # print(type(len(r.json()['body']['list'])))
        a=len(r.json()['body']['list'])

        print(random.randint(-1,a))

        num=random.randint(-1,a)
        print(r.json()['body']['list'][num]['institutionId'])
        print(r.json()['body']['list'][num]['institutionName'])
        print(r.json()['body']['list'][num]['campusId'])
        print(r.json()['body']['list'][num]['campusName'])


if __name__ == '__main__':
    unittest.main(verbosity=2)


