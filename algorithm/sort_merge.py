# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/21 15:10
@ FileName     : sort_merge.py
@ Description  : 归并排序
"""


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    i_left, i_right = 0, 0
    while len(result) <= len(left) + len(right):
        if left[i_left] < right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        if i_left >= len(left):
            result += right[i_right:]
            break
        if i_right >= len(right):
            result += left[i_left:]
            break
    return result


def merge_sort(arry):
    if len(arry) < 2:
        return arry

    midpoint = len(arry) // 2

    return merge(merge_sort(arry[:midpoint]), merge_sort(arry[midpoint:]))


a = [8, 2, 6, 4, 5]
r = merge_sort(a)
