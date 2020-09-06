# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/17 23:32
@ FileName     : sort_xuanze.py
@ Description  : 选择排序
"""

a = [int(_) for _ in input().split()]
# a = [2, 9, 4, 0, 1]
for i in range(len(a)):
    temp = i
    for j in range(i+1, len(a)):
        if a[j] < a[temp]:
            temp = j
    a[temp], a[i] = a[i], a[temp]
print(' '.join([str(_) for _ in a]))
