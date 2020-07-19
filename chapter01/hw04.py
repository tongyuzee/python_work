#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw04.py
@Time        :  2020/4/21 22:55
@Description :  None
"""
while True:
    try:
        sin = input('')
        x = 8 - len(sin) % 8
        x = x % 8
        sin1 = sin + '0' * x
        # print(sin1)
        for i in range(len(sin1) // 8):
            print(sin1[i * 8: i * 8 + 8])
    except:
        break
