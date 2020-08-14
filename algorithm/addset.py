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
a = input().split()
b = input().split()
print(' '.join(sorted(list(set(a+b)))))