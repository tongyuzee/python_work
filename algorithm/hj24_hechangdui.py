# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : hj24_hechangdui.py
@ Date & Time   : 2020/8/26 18:11
@ Description   : None
"""

"""
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   
则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
"""


def max_l(n, l):
    dps, dpj = [1] * n, [1] * n
    res = [0] * n
    for i in range(n):
        for j in range(i):
            if l[j] < l[i]:
                dps[i] = max(dps[j] + 1, dps[i])
    for i in reversed(range(n)):
        for j in reversed(range(i + 1, n)):
            if l[j] < l[i]:
                dpj[i] = max(dpj[j] + 1, dpj[i])
        if 0 < i < n - 1:
            res[i] = dpj[i] + dps[i] - 1
    return n - max(res)


def max_ll(n, l):
    dps, dpj = [1] * n, [1] * n
    res = 0
    for i in range(n):
        for j in range(i):
            if l[j] < l[i] and dps[j] + 1 > dps[i]:
                dps[i] = dps[j] + 1
            ri, rj = n - 1 - i, n - 1 - j
            if l[rj] < l[ri] and dpj[rj] + 1 > dpj[ri]:
                dpj[ri] = dpj[rj] + 1
    for i in range(1, n - 1):
        if dpj[i] > 1 and dps[i] > 1:
            res = max(res, dpj[i] + dps[i] - 1)
    return n - res


m = int(input())
p = [int(_) for _ in input().split()]
# m = 8
# p = [186, 186, 150, 200, 160, 130, 197, 200]
print(max_ll(m, p))
