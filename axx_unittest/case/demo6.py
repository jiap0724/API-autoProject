# -*- coding:utf-8 -*-
# @Time : 2021/5/24 17:48
# @Author : jiapeng
# @File : demo6.py
import unittest
import jsonpath
import requests
'''
接口关联

'''

class axx_learn(unittest.TestCase):

    @classmethod
    #初始化类方法
    def setUpClass(cls) -> None:
        cls.cookie=None
    # 登陆接口获取cookie
    def test_login(self):
        url='https://admin.aixuexi.com/shooter/manage/passwordLogin'
        data={
            'username':'jiapeng0@aixuexi.com',
            'password':'Jiapeng0724'
        }
        r=requests.post(url,data)
        axx_learn.cookie=r.cookies
        # cookies = r.cookies.items()
        # axx_learn.cookie = ''
        # for name, value in cookies:
        #     axx_learn.cookie += '{0}={1};'.format(name, value)
        # return axx_learn.cookie




    # 校区列表
    def test_xiaoqu(self):
        url = "http://oms.admin.aixuexi.com/marketingcenter/marketingactivity/institutions?pageNum=1&pageSize=10"
        r = requests.get(url, cookies=self.cookie, verify=False)
        print(r.text)
        key=input('请输入要获取的key:')
        value=jsonpath.jsonpath(r.json(),'$..{0}'.format(key)) #$表示最外层的{}，..表示模糊匹配
        # print(value)
        print(','.join('%s' %id for id in value))  #列表转换成string
        print(','.join(value))


if __name__ == '__main__':
    unittest.main()
