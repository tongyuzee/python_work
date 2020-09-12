# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : vivo
@ FileName      : vivo02.py
@ Date & Time   : 2020/9/12 20:25
@ Description   : None
"""

x = input().split(',')
f, j, a = '-1', 0, []
while True:
    b = []
    for i, v in enumerate(x):
        if v == f:
            b.append(str(i))
    if b:
        a.extend(sorted(b))
        f = a[j]
        j += 1
    else:
        break
print(','.join(a))
