# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : password.py
@ Date & Time   : 2020/8/13 19:14
@ Description   : None
"""

d = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4',
     'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6',
     'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8',
     'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}

p = input()
c = []
for v in p:
    if v.isupper():
        if v == 'Z':
            c.append('a')
        else:
            c.append(chr(ord(v.lower())+1))
    elif v.islower():
        c.append(d[v])
    else:
        c.append(v)
print(''.join(c))
