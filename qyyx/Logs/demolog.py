# -*- coding:utf-8 -*-
# @Time : 2021/2/4 18:50
# @Author : jiapeng
# @File : demolog.py
'''
log文件配置

'''
import logging

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='/Users/jiapeng/Downloads/pythonProject1/qyyx/Logs/log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式
