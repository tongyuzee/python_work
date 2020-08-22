# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/22 22:03
@ FileName     : sort_quick.py
@ Description  : 快速排序
"""


def quicksort(arry):
    if len(arry) < 2:
        return arry
    else:
        key = arry[len(arry)//2]
        little, equal, large = [], [], []
        for v in arry:
            if v < key:
                little.append(v)
            elif v == key:
                equal.append(v)
            else:
                large.append(v)
        return quicksort(little) + equal + quicksort(large)


a = [8, 6, -4, 9, 10]
r = quicksort(a)
print(' '.join([str(_) for _ in r]))
