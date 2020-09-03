# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : ceshi0903
@ Date & Time  : 2020/9/3 13:08
@ FileName     : base_conversion.py
@ Description  : 进制转换
"""


def conv10_n(m, n):
    m = int(m)
    n = int(n)
    r = []
    while m // n != 0:
        r.append(str(m % n))
        m = m // n
    r.append(str(m))
    return ''.join(reversed(r))


def convn_10(m, n):
    n = int(n)
    r = 0
    for i, v in enumerate(reversed(list(m))):
        r += int(v) * (n ** i)
    return str(r)


x, y = input().split()
z = conv10_n(x, y)
print(z)
print(convn_10(z, y))
