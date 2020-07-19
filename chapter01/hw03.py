#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw03.py
@Time        :  2020/4/21 17:23
@Description :  None
"""

while True:
    try:
        n = int(input(''))
        num_i = []
        counter = 0
        while counter < n:
            x = int(input(''))
            if x not in num_i:
                num_i.append(x)
            counter += 1
        num_i.sort()
        for y in num_i:
            print(y)
    except :
        break
