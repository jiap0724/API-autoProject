# -*- coding:utf-8 -*-
# @Time : 2021/5/18 11:26
# @Author : jiapeng
# @File : demo1.py
'''
unittest的基本用法
'''

#导入unittest
import unittest
#通过继承unittest中的TestCase 来实现测试用例的继承
class axx_learn(unittest.TestCase):
    #类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print('clssetUp')

    #类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print('clstearDown')


    # 前置条件
    def setUp(self) -> None:
        print('setUp')
        self.age=input('年龄:')
        return self.age


    # 后置条件
    def tearDown(self) -> None:
        print('tearDown')

    # def age(self):
    #     age=input('年龄:')
    #     return age

    # 测试用例要使用test命名，以此来识别要执行的测试用例
    def test_shanshan(self):
        print('I am shanshan and '+self.age+' years old')

    def test_chengcheng(self):
        print('I am chengcheng')



if __name__ == '__main__':
    unittest.main(verbosity=2)
