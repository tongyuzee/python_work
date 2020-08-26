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


def max_l(l):
    n = len(l)
    dps, dpj = [1] * n, [1] * n
    res = 0
    for i in range(n):
        for j in range(i):
            if l[j] < l[i]:
                dps[i] = max(dps[j]+1, dps[i])
            if l[j] > l[i]:
                dpj[i] = max(dpj[j] + 1, dpj[i])

        res = max(res, dpj[i] + dps[i] - 1)
    return res


m = max_l([186, 186, 150, 200, 160, 130, 197, 200])
