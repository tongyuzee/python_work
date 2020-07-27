# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/27 21:29
@ FileName     : zishoushu.py
@ Description  : 自守数，例如 25 * 25 = 625， 6 * 6 = 36
"""


def zishou(n):
    z = []
    for v in range(n + 1):
        if v * v % (10 ** len(list(str(v)))) == v:
            z.append(v)
    return z


N = int(input())
zs = zishou(N)
print(len(zs))
