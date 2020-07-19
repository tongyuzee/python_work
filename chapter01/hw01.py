#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw01.py
@Time        :  2020/4/20 23:09
@Description :  None
"""

x = input('')
x = ' ' + x
i = -1
counter = 0
while x[i] != ' ':
    counter = counter + 1
    i = i - 1
print(counter)
