# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : zuichangzichuan.py
@ Date & Time   : 2020/7/30 16:04
@ Description   : 最长字串
"""

s = input()

l = 0
a = []
for v in s:
    while v in a:
        a.pop(0)
    a.append(v)
    if len(a) > l:
        l = len(a)
print(l)


