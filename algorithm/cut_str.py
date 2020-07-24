# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/24 21:10
@ FileName     : cut_str.py
@ Description  : 字符串分割
"""


def cutstr(s):
    a = (8 - len(s) % 8) % 8
    ss = s + '0' * a
    sp = []
    for i in range(len(ss) // 8):
        sp.append(ss[i * 8: (i + 1) * 8])
    return sp


N = int(input())
for j in range(N):
    for y in cutstr(input()):
        print(y)

# 简单方法
N = int(input())
for j in range(N):
    x = input()
    while len(x) > 8:
        print(x[:8])
        x = x[8:]
    print(x.ljust(8, '0'))
