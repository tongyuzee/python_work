# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : sort_dict.py
@ Date & Time   : 2020/8/2 14:16
@ Description   : 按照字典的value值排序
"""

"""商品名称与数量"""
goods = dict(A1=2, A6=8, A4=9, A7=4, A5=2, A2=3, A8=5, A3=9, A9=1)

print("按照商品名称排序：")
for g in sorted(goods.keys()):
    print('{} : {}'.format(g, goods[g]))

print("按照商品数量排序：")
for g in sorted(goods.keys(), key=lambda x: goods[x]):
    print('{} : {}'.format(g, goods[g]))

print("按照商品数量排序（逆序）：")
for g in sorted(goods.keys(), key=lambda x: goods[x], reverse=True):
    print('{} : {}'.format(g, goods[g]))
