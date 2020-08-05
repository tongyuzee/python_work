# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/5 21:17
@ FileName     : sortstr.py
@ Description  : None
"""

a, n = [], int(input())
for i in range(n):
    a.append(input())
for v in sorted(a):
    print(v)
