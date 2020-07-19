#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw08.py
@Time        :  2020/5/1 23:47
@Description :  None
"""

n = int(input(''))
z = {}
for i in range(n):
    x = list(map(int, input('').split()))
    if x[0] in z.keys():
        z[x[0]] += x[1]
    else:
        z[x[0]] = x[1]

for k in sorted(z.keys()):
    print(str(k) + ' ' + str(z[k]))
