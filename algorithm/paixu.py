# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : paixu.py
@ Date & Time   : 2020/7/26 21:33
@ Description   : None
"""
"""bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。"""

n, x, flag = int(input()), [int(v) for v in input().split()], int(input())
y = [str(v) for v in sorted(x, reverse=bool(flag))]
print(' '.join(y))
