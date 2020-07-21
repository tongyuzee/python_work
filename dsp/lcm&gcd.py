# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : dsp
@ FileName      : lcm&gcd.py
@ Date & Time   : 2020/7/21 11:42
@ Description   : 求最大公约数（GCD）与最小公倍数(LCM)
"""


def gcd(m, n):
    """
    求最大公约数(Greatest Common Divisor(GCD))
    辗转相除法
    """
    if m < n:
        m, n = n, m
    yushu = m % n
    while yushu != 0:
        m, n = n, yushu
        yushu = m % n
    return n


def lcm(m, n):
    """
    求最小公倍数(Least Common Multiple(LCM))
    两个数的乘积等于这两个数的最大公约数与最小公倍数的积，即（a，b）×[a，b]=a×b。
    """
    return m * n // gcd(m, n)


x = input('').split()
print("{}和{}的最大公约数为：{}".format(x[0], x[1], gcd(int(x[0]), int(x[1]))))
print("{}和{}的最小公倍数为：{}".format(x[0], x[1], lcm(int(x[0]), int(x[1]))))
