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
# a = [2, 9, 4, 0, 1]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(' '.join([str(_) for _ in a]))
