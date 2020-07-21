# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : curt.py
@ Date & Time   : 2020/7/21 14:34
@ Description   : 求立方根
"""

def curt(n):
    """求n的立方根"""
    i = 0.0001
    while i**3 < n:
        i += 0.04
    return i


x = float(input())
print("{:.1f}".format(curt(x)))
print("{}".format(curt(x)))

