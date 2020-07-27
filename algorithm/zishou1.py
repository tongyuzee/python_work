# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/27 21:43
@ FileName     : zishou1.py
@ Description  : 自守数，例如 25 * 25 = 625， 6 * 6 = 36
"""


def zishou(n):
    z = []
    for v in range(n + 1):
        if str(v * v).endswith(str(v)):
            z.append(v)
    return z


N = int(input())
zs = zishou(N)
print(len(zs))

print(len([v for v in range(int(input())+1) if str(v * v).endswith(str(v))]))

print(len(list(filter(lambda c: str(c**2).endswith(str(c)), range(int(input()))))))
