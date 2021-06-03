# -*- coding:utf-8 -*-
# @Time : 2021/5/23 19:07
# @Author : jiapeng
# @File : HttpRequest.py
'''
请求方法封装
'''
import json

import jsonpath
import requests

class HttpRequest:
    # get请求方法
    def http_get(self, url,header,param):
        return requests.get(url=url,headers=header,params=param)

    # post请求方法
    def http_post(self,url,header,data):
        return requests.post(url=url,headers=header,json=data)

    # post请求方法
    def http_post_data(self,url,header,data):
        return requests.post(url=url,headers=header,data=data)

#    获取参数值
    def get_msg(self,r,key):
        if r is not None:
            try:
                msg=json.loads(r)
                value=jsonpath.jsonpath(msg,'$..{0}'.format(key))
                if value:
                    if len(value)==1:
                        return value[0]
                return value

            except Exception as e:
                return e
        else:
            return None





