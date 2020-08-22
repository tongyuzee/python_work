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
        key = arry[0]
        little, equal, large = [], [], []
        for v in arry:
            if v < key:
                little.append(v)
            elif v == key:
                equal.append(v)
            else:
                large.append(v)
        return quicksort(little) + equal + quicksort(large)


a = [3, 6, -4, 9, 0]
r = quicksort(a)
print(' '.join([str(_) for _ in r]))
