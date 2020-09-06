# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : Fluent_Py
@ Date & Time   : 2020/9/6 19:56
@ FileName      : tencent01.py
@ Description   : None
"""

m = input()
a = input().split()
n = input()
b = input().split()
for v in b:
    if v in a:
        print(v, end=' ')
