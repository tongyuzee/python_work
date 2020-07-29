# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : convertRMB.py
@ Date & Time   : 2020/7/29 16:15
@ Description   : 人民币转换大写
"""

num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
dan = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
fen = ['角', '分']

x = input().split('.')
a = []
if x[0] != '0':
    for i, v in enumerate(x[0][::-1]):
        if v == '0' and i not in [0, 4, 8]:
            a.append('零')
        else:
            a.append(num[int(v)] + dan[i])

b = []
if x[-1] in ['00', '0']:
    b.append('整')
else:
    for i, v in enumerate(x[-1]):
        if v == '0':
            continue
        else:
            b.append(num[int(v)] + fen[i])

rmb = '人民币'+''.join(a[::-1]+b)
rmb = rmb.replace('壹拾', '拾')
while '零零' in rmb:
    rmb = rmb.replace('零零', '零')
rmb = rmb.replace('零元', '元')
rmb = rmb.replace('零万', '万')
rmb = rmb.replace('零亿', '亿')
print(rmb)
