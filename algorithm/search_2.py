# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : search_2.py
@ Date & Time   : 2020/8/25 17:02
@ Description   : 二分查找
"""


def search2(n, v, a):
    midp = (n + 1) // 2
    if a[midp] == v:
        temp = midp
        while a[temp-1] == v:
            temp -= 1
        r
