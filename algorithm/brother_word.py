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
    if v != w and sorted(list(v)) == sorted(list(w)):
        a.append(v)
print(len(a))
print(a[int(m)-1])