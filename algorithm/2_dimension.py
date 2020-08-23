# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/23 21:56
@ FileName     : 2_dimension.py
@ Description  : 二维列表
"""

# 创建一个包含3个列表的列表，被包含的3个列表各自有3个元素
# 修改其中某一个列表的元素，其余列表不会改变
b = [['-'] * 3 for _ in range(3)]
b[1][2] = 'X'
print(b)

# 外面的列表其实包含3个指向同一个列表的引用
# 修改其中一个列表的元素，其余的列表也会随之改变
c = [['-'] * 3] * 3
c[1][2] = 'X'
print(c)
