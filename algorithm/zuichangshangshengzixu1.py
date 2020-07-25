# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/25 14:36
@ FileName     : zuichangshangshengzixu1.py
@ Description  : 最长上升子序牛逼算法
"""

import bisect

a, b = int(input()), map(int, input().split())
q = []
for v in b:
    pos = bisect.bisect_left(q, v)
    if pos == len(q):
        q.append(v)
    else:
        q[pos] = v
print(len(q))
