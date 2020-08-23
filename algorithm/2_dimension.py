# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/23 21:56
@ FileName     : 2_dimension.py
@ Description  : 二维列表
"""

b = [['-'] * 3 for _ in range(3)]
b[1][2] = 'X'
print(b)

c = [['-'] * 3] * 3
c[1][2] = 'X'
print(c)
