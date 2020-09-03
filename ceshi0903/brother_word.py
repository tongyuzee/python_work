# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : brother_word.py
@ Date & Time   : 2020/8/13 17:21
@ Description   : 查找兄弟单词
"""

n, *d, w, m = input().split()

a = []
for v in d:
    if len(v) == len(w) and v != w and set(v) == set(w) and sorted(list(v)) == sorted(list(w)):
        a.append(v)
print(len(a))
if a:
    print(a[int(m)-1])