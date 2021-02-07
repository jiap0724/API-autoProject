# -*- coding:utf-8 -*-
# @Time : 2021/2/4 18:55
# @Author : jiapeng
# @File : log_info.py
import logging
import json
from qyyx.Logs.demolog import *

def log_case_info(case_name, url, data, res_text):
    if isinstance(data,dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    # logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))
