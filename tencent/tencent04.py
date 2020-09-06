# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : tencent
@ Date & Time   : 2020/9/6 20:53
@ FileName      : tencent04.py
@ Description   : None
"""
n = int(input())
x = [int(_) for _ in input().split()]
z = sorted(x)
for i in range(n):
    y = z[:]
    y.remove(x[i])
    print(y[n//2-1])
