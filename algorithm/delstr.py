# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/9 22:06
@ FileName     : delstr.py
@ Description  : 删除字符串中出现次数最少的字符后的字符串
"""
"""
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
"""

s = list(input())
d = {}
for v in set(s):
    c = s.count(v)
    if c in d.keys():
        d[c] += v
    else:
        d[c] = v
p = min(d.keys())
for i in d[p]:
    while i in s:
        s.remove(i)
print(''.join(s))
