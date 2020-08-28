# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/28 21:33
@ FileName     : match_brackets.py
@ Description  : 括号匹配
"""

s = input()
b = []
for i, v in enumerate(s):
    if v in ['(', '[', '{']:
        b.append(v)
    elif v == ')':
        if b and b[-1] == '(':
            b.pop()
        else:
            b.append(v)
    elif v == ']':
        if b and b[-1] == '[':
            b.pop()
        else:
            b.append(v)
    elif v == '}':
        if b and b[-1] == '{':
            b.pop()
        else:
            b.append(v)
