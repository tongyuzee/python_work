# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : digui_fun.py
@ Date & Time   : 2020/8/21 17:09
@ Description   : 函数的递归调用
"""


def fun(n):
    if n == 0:
        return 1
    else:
        return n * fun(n)


print(fun(5))
