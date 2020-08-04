# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : zuichangshuzi.py
@ Date & Time   : 2020/8/4 17:09
@ Description   : 在字符串中找出连续最长的数字串
"""

x = input()
a = []
for v in x:
    if v.isdecimal():
        a.append('*' + v + '*')
    else:
        a.append(v)
b = ''.join(a).replace('**', '')
c = [v for v in b.split('*') if v.isdecimal()]
d = {}
for v in c:
    if len(v) in d.keys():
        d[len(v)] += v
    else:
        d[len(v)] = v
m = max(d.keys())
print("{},{}".format(d[m], m))



