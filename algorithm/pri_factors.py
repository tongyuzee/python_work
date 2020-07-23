# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/23 22:08
@ FileName     : pri_factors.py
@ Description  : 求正整数的质数因子（牛逼的算法1）
"""
import math

a, res = int(input()), []

for i in range(2, int(math.sqrt(a)) + 1):
    """从i=2开始，用a除以i，直到除不尽为止，i++，如此循环直到i等于sqrt(a)"""
    while a % i == 0:
        a = a / i
        res.append(i)
print(" ".join(map(str, res)) + " " if res else str(a) + " ")
