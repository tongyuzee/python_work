# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/5 21:04
@ FileName     : countstr.py
@ Description  : 统计字符
"""

a = set(input())
b = [v for v in a if 0 <= ord(v) <= 127]
print(len(b))
