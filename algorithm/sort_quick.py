# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/22 22:03
@ FileName     : sort_quick.py
@ Description  : 快速排序
"""
from random import choice


def quicksort(arry):
    if len(arry) < 2:
        return arry
    else:
        # 选择任意一个元组作为比较对象
        # key = arry[0]
        # 当key为中位数时，排序最快，随机选择一个数，选择到中位数的概率更大
        key = arry[choice(range(len(arry)))]
        little, equal, large = [], [], []
        for v in arry:
            if v < key:
                little.append(v)
            elif v == key:
                equal.append(v)
            else:
                large.append(v)
        return quicksort(little) + equal + quicksort(large)


a = [3, 6, -4, 9, 0, 0, 1, 2, 3, 5, 7, 8, 11, -45, 1000, 34, 67]
r = quicksort(a)
print(' '.join([str(_) for _ in r]))
