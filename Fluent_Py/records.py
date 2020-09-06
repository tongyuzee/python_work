# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : records.py
@ Date & Time   : 2020/8/20 16:19
@ Description   : 简单错误记录
"""
r = []
while True:
    s = input().replace('\\', '/')
    if s == '':
        break
    else:
        r.append(s)
d = {}
for v in r[-8:]:
    u = v.split()
    p = u[0].split('/')
    e = p[-1][-16:] + ' ' + u[-1]
    if e in d.keys():
        d[e] += 1
    else:
        d[e] = 1
for k, v in d.items():
    print("{} {}".format(k, v))
