# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : ceshi0903
@ Date & Time  : 2020/9/3 12:26
@ FileName     : sort_dict.py
@ Description  : None
"""

"""商品名称与数量"""
goods = dict(A1=5, A6=5, A4=9, A7=9, A5=2, A2=3, A8=5, A3=9, A9=1)

print("按照商品名称排序：")
for g in sorted(goods.keys()):
    print('{} : {}'.format(g, goods[g]))

print("按照商品数量排序：")
for g in sorted(goods.keys(), key=lambda x: goods[x]):
    print('{} : {}'.format(g, goods[g]))

print("按照商品数量排序（逆序）：")
for g in sorted(sorted(goods.keys(), reverse=True), key=lambda x: goods[x], reverse=True):
    """先按照keys排序，再按照values排序"""
    print('{} : {}'.format(g, goods[g]))
