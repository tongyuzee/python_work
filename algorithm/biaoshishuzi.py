# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : biaoshishuzi.py
@ Date & Time   : 2020/7/29 13:51
@ Description   : 表示数字
"""

'''复杂方法'''
x = input()
a = [0]
for i in range(0, len(x)-1):
    y = x[i:i+2]
    if not y.isdigit() and not y.isalpha():
        a.append(i+1)
b = [x[a[i-1]:a[i]] for i in range(1, len(a))]
b.append(x[a[-1]:])
for i in range(len(b)) :
    if b[i].isdigit():
        b[i] = '*' + b[i] + '*'
print(''.join(b))

'''简单方法'''
x = input()
a = []
for v in x:
    if v.isalpha():
        a.append(v)
    else:
        a.append("*" + v + "*")
print(''.join(a).replace('**', ''))
