# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : addset.py
@ Date & Time   : 2020/8/14 17:24
@ Description   : None
"""
n, m = input().split()
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
for k in sorted(list(set(a+b))):
    print(k, end=' ')
