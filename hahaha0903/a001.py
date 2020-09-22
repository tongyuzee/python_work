# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : hahaha0903
@ Date & Time  : 2020/9/3 14:38
@ FileName     : a001.py
@ Description  : None
"""

a = [-1, 1, 2, 3, 4, -100, 1, 2, 3, 4, 0, -1, 10]
sum_l, sum_j = [0] * 3, [0] * 3
for l in range(1, len(a)):
    sum_j = [0] * 3
    for i in range(len(a)):
        j = i + l
        if j > len(a):
            break
        if sum(a[i: j+1]) > sum_j[0]:
            sum_j[0] = sum(a[i: j])
            sum_j[1] = i
            sum_j[2] = j
    if sum_j[0] >= sum_l[0]:
        sum_l = sum_j[:]

print(sum_l)
