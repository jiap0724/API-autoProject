# -*- coding:utf-8 -*-
# @Time : 2021/5/23 19:07
# @Author : jiapeng
# @File : HttpRequest.py
'''
请求方法封装
'''
import json
import requests

class HttpRequest:

    def http_request(self, url, data, http_method, cookie,header):
        try:

            if http_method.upper() == 'GET':
                res = requests.get(url,  cookies=cookie,headers=header,verify=False)  #使用verify=False 解决 HTTPSConnectionPool(host='***', port=443)
            elif http_method.upper() == 'POST':
                res = requests.post(url, data, cookies=cookie,headers=header,verify=False)
            else:
                print("请求方法错误 不是get、post请求方法 ！")
        except Exception as e:
            print("请求出错了：{0}".format(e))

        return res.json()
        # return json.dumps(res.json(),ensure_ascii=False,indent=2,sort_keys=True)



