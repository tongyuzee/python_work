# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : zuichangzichuan.py
@ Date & Time   : 2020/7/30 16:04
@ Description   : 最长字串
"""

"""
这道题主要用到思路是：滑动窗口
比如例题中的 abcabcbb，进入这个窗口为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
"""

s = input()

l = 0
a, b = [], []
for v in s:
    while v in a:
        a.pop(0)
    a.append(v)
    if len(a) > l:
        l = len(a)
        b = a[:]
print(l)
print(''.join(b))
