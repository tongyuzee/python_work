# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : zuichangzichuan.py
@ Date & Time   : 2020/7/30 16:04
@ Description   : 最长字串
"""

s = "asjrgapa"

l = 0
for i in range(len(s)):
    a = []
    b = []
    for v in s[i:]:
        if v not in a:
            a.append(v)
        else:
            if len(a) > l:
                l = len(a)
            b.append(a)
            a = [v]
    b.append(a)
    if len(a) > l:
        l = len(a)
print(l)
