# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : tencent
@ Date & Time   : 2020/9/6 21:10
@ FileName      : tencent03.py
@ Description   : None
"""

n, k = [int(_) for _ in input().split()]
s = []
for i in range(n):
    s.append(input())
d = {}
for v in s:
    if v not in d.keys():
        d[v] = s.count(v)
y = sorted(sorted(d.keys()), key=lambda x: d[x], reverse=True)
for i in range(k):
    print(y[i], d[y[i]])
y = sorted(sorted(d.keys()), key=lambda x: d[x])
for i in range(k):
    print(y[i], d[y[i]])
