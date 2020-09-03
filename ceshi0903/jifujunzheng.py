# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : jifujunzheng.py
@ Date & Time   : 2020/7/29 13:41
@ Description   : 记负均正
"""

n = int(input())
y = [int(v) for v in input().split()]
fu = 0
zh = 0
sz = 0
for x in y:
    if x < 0:
        fu += 1
    elif x > 0:
        sz += x
        zh += 1
print("{} {:.1f}".format(fu, sz/zh))
