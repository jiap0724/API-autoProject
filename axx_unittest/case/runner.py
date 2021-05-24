# -*- coding:utf-8 -*-
# @Time : 2021/5/19 11:45
# @Author : jiapeng
# @File : runner.py
import unittest

from axx_unittest.case.demo4 import axx_learn

# suite = unittest.TestSuite()
# # suite.addTest(axx_learn('test_login')) # 添加单个用例
# suite.addTests([axx_learn('test_login'),axx_learn('test_login1')]) # 添加多个用例
# # 运行测试集
# unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序


suite1 = unittest.makeSuite(axx_learn, 'test_login001') # 使用测试类的单条用例制作测试集
suite2 = unittest.makeSuite(axx_learn) # 使用整个测试类制作测试集合(包含该测试类所有用例)

unittest.TextTestRunner(verbosity=2).run(suite1)
