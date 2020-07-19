#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw001.py
@Time        :  2020/4/22 19:01
@Description :  None
"""

x = input('')
y = []
for v in x:
    if '0' <= v <= '9':
        y.append(v)
y.sort()
s = ''.join(y)
print(s)

# 利用列表推导式一行代码可以实现上述功能
print(''.join(sorted([v for v in input('') if '0' <= v <= '9'])))
