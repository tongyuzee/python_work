# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/27 21:43
@ FileName     : zishou1.py
@ Description  : 自守数，例如 25 * 25 = 625， 6 * 6 = 36
"""

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
最后将返回 True 的元素放到新列表中。
"""


def zishou(n):
    z = []
    for v in range(n + 1):
        if str(v * v).endswith(str(v)):
            z.append(v)
    return z


N = int(input())
zs = zishou(N)
print(len(zs))

# 一行代码
print(len([v for v in range(int(input())+1) if str(v * v).endswith(str(v))]))

print(len(list(filter(lambda c: str(c**2).endswith(str(c)), range(int(input()))))))
