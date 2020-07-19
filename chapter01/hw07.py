#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw07.py
@Time        :  2020/4/22 17:33
@Description :  None
"""

x = input('')
y = []
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])

s = ''.join(y)
print(s)
