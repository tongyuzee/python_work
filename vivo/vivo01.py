# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : vivo
@ FileName      : vivo01.py
@ Date & Time   : 2020/9/12 19:54
@ Description   : None
"""


def ishui(s):
    i, j = 0, len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


x = list(input())
flag = False
for v in range(len(x)):
    y = x[:]
    y.pop(v)
    if ishui(y):
        print(''.join(y))
        flag = True
        break
if not flag:
    print('false')
