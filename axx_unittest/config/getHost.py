# -*- coding:utf-8 -*-
# @Time : 2021/6/3 20:51
# @Author : jiapeng
# @File : getHost.py
'''
获取host配置
'''
import configparser
def GetHost(path,selector,host):
    conf=configparser.ConfigParser()
    conf.read(path)
    return conf.get(selector,host)

