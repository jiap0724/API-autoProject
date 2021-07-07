# -*- coding:utf-8 -*-
# @Time : 2021/6/28 15:26
# @Author : jiapeng
# @File : demo9.py
import unittest

from axx_unittest.GetCookie import GetHeader


class demo9(unittest.TestCase):
    def test_demo9(self):
        ptpc=GetHeader.test_Getptpc
        # userid=GetHeader.Getuserid()
        print('ptpc:'+ptpc)
        # print('userid:'+userid)
