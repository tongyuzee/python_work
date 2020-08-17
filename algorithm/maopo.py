# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/17 23:00
@ FileName     : maopo.py
@ Description  : 冒泡排序
"""

a = [int(_) for _ in input().split()]
for i in range(len(a)):
    for j in range(1, len(a)-i):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(' '.join([str(_) for _ in a]))
