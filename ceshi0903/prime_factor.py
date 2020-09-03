# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/23 21:24
@ FileName     : prime_factor.py
@ Description  : 求正整数的质数因子
"""
import math


def isprime(n):
    """判断n是否为质数"""
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True


def primes(n):
    """生成若干素数"""
    p = []
    for i in range(2, n+1):
        if isprime(i):
            p.append(i)
    return sorted(p)


x = int(input())
pr = primes(x)

p_factor = []
while x != 1:
    for j in pr:
        if x % j == 0:
            p_factor.append(str(j))
            x = x // j
            print(j, end=' ')
            break

# print(' '.join(p_factor))
