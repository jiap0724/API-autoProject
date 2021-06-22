# -*- coding:utf-8 -*-
# @Time : 2021/6/22 18:10
# @Author : jiapeng
# @File : demo.py
import random
a = [1,2,3,4,5]
#1
print(random.choices(a,k=10))
#2
print(random.choices(a,weights=[0,0,0,1,0],k=5))
#3
print(random.choices(a,weights=[1,1,1,1,1],k=5))
#4
print(random.choices(a,cum_weights=[1,1,1,1,1],k=5))

print(random.choice(a))
#1 ： 重复输出10次列表a中的各个成员出现概率基本持平。
#2 ： 重复输出10次每次输出均得到[3,3,3,3,3]结果。
#3 ： 重复输出10次列表a中的各个成员出现概率基本持平。
#4 ： 重复输出10次每次输出均得到[1,1,1,1,1]结果。
