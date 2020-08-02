# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : vectors.py
@ Date & Time   : 2020/8/2 15:41
@ Description   : 构建向量类（Vector）
"""

import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        """向量的模"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """向量加法"""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """向量的数乘"""
        return Vector(self.x * other, self.y * other)


v1 = Vector(2, 4)
v2 = Vector(1, 2)
print(v1 + v2)

print(abs(Vector(3, 4)))

print(v1 * 3)
