#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw06.py
@Time        :  2020/4/22 17:29
@Description :  None
"""
while True:
    try:
        x = input('')
        x.strip()
        y = x.split()
        s = int(y[0]) + int(y[1])
        print(s)
    except:
        break