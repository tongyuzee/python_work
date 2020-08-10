# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : fibonacci.py
@ Date & Time   : 2020/8/10 20:43
@ Description   : 斐波那契数列
"""


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        a, b = 1, 1
        for i in range(3, n+1):
            a, b = b, a+b
        return b


x = int(input())
f = []
for j in range(1, x+1):
    f.append(fib(j))
print(f)

print(fib(int(input())))