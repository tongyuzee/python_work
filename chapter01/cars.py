#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  cars.py
@Time        :  2020/4/16 0:05
@Description :  None
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()         # 方法sort() 永久性地改变元素顺序，默认升序排列
print(cars)
cars.sort(reverse=True)         # 降序排列
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\n打印原始列表：')
print(cars)
s_cars = sorted(cars)           # 函数sorted() 临时改变元素顺序，默认升序
print('\n打印升序排列后的列表：')
print(s_cars)
sr_cars = sorted(cars, reverse=True)        # 降序排列
print('\n打印降序排列后的列表：')
print(sr_cars)
print('\n再次打印原始列表：')    # 原始列表顺序不变
print(cars)

cars.reverse()       # 方法reversed() 永久性地反转列表元素顺序，不是按照字母顺序
print('\n打印倒序排列的列表：')
print(cars)

print(len(cars))
