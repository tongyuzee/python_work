# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/19 22:50
@ FileName     : move_position.py
@ Description  : 坐标移动
"""


def move(p, d1, d2):
    """
    坐标移动
    :param p: 坐标 [x,y]
    :param d1: 方向 A W S D
    :param d2: 距离
    """
    if d1 == 'A':
        p[0] -= d2
    elif d1 == 'D':
        p[0] += d2
    elif d1 == 'W':
        p[1] += d2
    elif d1 == 'S':
        p[1] -= d2


a = [0, 0]
for cmd in input().split(';'):
    if 0 < len(cmd) <= 3 and cmd[0] in ['A', 'W', 'S', 'D'] and cmd[1:].isdecimal():
        move(a, cmd[0], int(cmd[1:]))
print("{},{}".format(a[0], a[1]))
