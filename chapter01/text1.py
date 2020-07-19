#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  text1.py
@Time        :  2020/4/28 15:45
@Description :  None
"""


def ree(x):
    x1 = x.split()
    x2 = reversed(x1)
    return ' '.join(x2)


s = 'I am a boy'
s1 = ree(s)
print(s1)
# y = x.split()
#
# c3 = []
# for b in y:
#     c = list(b)
#     c1 = reversed(c)
#     c2 = ''.join(c1)
#     c3.append(c2)
#
# v = reversed(c3)
# z = ' '.join(v)
# print(z)

zn = ''.join([s[i] for i in reversed(list(range(-len(s), 0)))])
print(zn)

print(''.join(reversed(list(s))))
print('hello', end='')
print('world')
