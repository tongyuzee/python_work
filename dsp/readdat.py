# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/15 18:12
# @FileName     : readdat.py
# @Software     : PyCharm
# --------------

import csv

with open("sig.dat", 'r') as f:
    reader = csv.reader(f)
    sig = list(reader)

# 列表推导式的嵌套
data1 = [[float(x) for x in y] for y in sig]
# map()函数的嵌套
data2 = list(map(lambda x: list(map(float, x)), sig))
# 列表推导式与map()函数的互相嵌套 1
data3 = [list(map(float, x)) for x in sig]
# 列表推导式与map()函数的互相嵌套 2
data4 = list(map(lambda y: [float(x) for x in y], sig))
