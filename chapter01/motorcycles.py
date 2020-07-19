#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  motorcycles.py
@Time        :  2020/4/15 23:43
@Description :  None
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'       # 直接修改列表元素
print(motorcycles)

motorcycles.append('honda')     # 在列表末尾添加元素
print(motorcycles)

motorcycles.insert(0, 'motor0')     # 在指定位置添加元素，之后的元素后移一位
print(motorcycles)
motorcycles.insert(2, 'motor2')     # 在指定位置添加元素，之后的元素后移一位
print(motorcycles)

del motorcycles[2]      # del语句 直接删除指定的元素
print(motorcycles)

popped_motor = motorcycles.pop(0)       # 方法pop 删除指定元素（索引为空时，默认删除末尾元素），并且可以所存储删除的元素
print(motorcycles)
print(popped_motor)

motorcycles.remove('yamaha')        # 方法remove 根据元素值删除元素，当需要删除的元素多次出现时，仅删除第一个元素
print(motorcycles)
