# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : count_char.py
@ Date & Time   : 2020/7/26 20:31
@ Description   : 字符统计
"""

s = input()
x = set(s)

d = {}
for v in x:
    if 'a' <= v.lower() <= 'z' or '0' <= v <= '9' or v == ' ':
        num = s.count(v)
        if num in d.keys():
            d[num].append(v)
        else:
            d[num] = [v]

p = []
for k in sorted(d.keys(), reverse=True):
    print(''.join(sorted(d[k])), end='')
    # p.append(''.join(sorted(d[k])))
print()
