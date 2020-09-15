# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : hahaha0903
@ Date & Time  : 2020/9/3 16:23
@ FileName     : a002.py
@ Description  : None
"""


class Date:

    def __init__(self, s):
        self.date = {}
        j = 0
        for i, v in enumerate(s):
            if v in '年月日时分秒':
                self.date[v] = s[j:i]
                j = i+1

    def pri0(self):
        print('.'.join(list(self.date.values())[:3]), ':'.join(list(self.date.values())[-3:]))

    def pri1(self):
        print('-'.join(list(self.date.values())[:3]), '-'.join(list(self.date.values())[-3:]))

    def pri2(self):
        print(''.join(list(self.date.values())[:3]), ''.join(list(self.date.values())[-3:]))


x = '2020年09月03日16时34分40秒'
a = Date(x)
a.pri0()
a.pri1()
a.pri2()
