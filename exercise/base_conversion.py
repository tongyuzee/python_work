# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : ceshi0903
@ Date & Time  : 2020/9/3 13:08
@ FileName     : base_conversion.py
@ Description  : 禁止转换
"""


def conv10_n(m, n):
    m = int(m)
    r = ''
    while m // n != 0:
        r += str(m % n)
        m = m // n
    return r


x, y = input().split()
print(conv10_n(x, y))
