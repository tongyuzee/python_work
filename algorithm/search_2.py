# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : search_2.py
@ Date & Time   : 2020/8/25 17:02
@ Description   : 二分查找
"""
import bisect


def search2(n, v, a):

    if n == 0:
        return -1

    midp = n // 2
    if a[midp] == v:
        while a[midp - 1] == v:
            midp -= 1
        return midp
    elif a[midp] > v:
        return search2(midp, v, a[:midp])
    else:
        return search2(n-midp-1, v, a[midp+1:])


def search_2(n, v, a):
    if v > a[n-1]:
        return n+1
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if v > a[mid]:
            l = mid + 1
        elif v <= a[mid]:
            r = mid
    return r+1


def s2(n, v, a):
    p = bisect.bisect_left(a, v)
    return p+1


y = [3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 12, 13, 15, 16, 21, 21, 22, 24, 24, 27, 28, 32, 34, 35, 35, 36, 36, 39, 40, 41,
     41, 42, 44, 44, 45, 45, 47, 47, 47, 47, 48, 48, 50, 51, 51, 53, 53, 53, 54, 54, 54, 56, 56, 57, 59, 60, 60, 60, 60,
     61, 62, 63, 65, 65, 65, 65, 67, 67, 68, 70, 71, 71, 74, 75, 75, 79, 81, 84, 84, 86, 86, 87, 90, 90, 90, 90, 91, 92,
     93, 94, 94, 94, 95, 97, 97, 98, 98, 99]
x = s2(100, 97, y)
print(x)
