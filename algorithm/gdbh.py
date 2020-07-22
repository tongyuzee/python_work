# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : dsp
@ FileName      : gdbh.py
@ Date & Time   : 2020/7/20 20:19
@ Description   : 哥德巴赫猜想
"""

import math


def isprime(n):
    """
    判断是否为素数
    素数是指除了 1 和它本身以外，不能被任何整数整除的数
    """
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def primes(n):
    """
    生成若干素数(prime)
    """
    q = [1]
    for i in range(2, n+1):
        if isprime(i):
            q.append(i)
    return q


def gedebahe(m, n):
    """
    任意一个大于2的整数都可以写成两个素数(包含1)之和
    """
    q = []
    nn = m - n
    ls = sorted(primes(nn))
    if nn % 2 != 0 or nn <= 2:
        q = [-1]
    else:
        for i in ls:
            if i != n and nn - i in ls:
                q = [i, nn - i]
                break
    return sorted(q)


T = int(input())
XY = []
for j in range(T):
    v = input().split()
    XY.append(v)

for row in XY:
    x = int(row[0])
    y = int(row[1])
    shang = x // y
    if x % y != 0 or shang < 6:
        print(-1)
        continue
    elif shang % 2 == 0:
        fenjie = [2] + gedebahe(shang, 2)
    else:
        fenjie = [3] + gedebahe(shang, 3)
    result = [str(y * k) for k in sorted(fenjie)]
    print(' '.join(result))

