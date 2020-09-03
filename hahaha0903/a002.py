# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : hahaha0903
@ Date & Time  : 2020/9/3 16:23
@ FileName     : a002.py
@ Description  : None
"""


class Convdate:

    def __init__(self, s):
        ss = ''
        for v in s:
            if not v.isdecimal():
                ss += '*'
            else:
                ss += v
        self.shuzi = ss.split('*')
        self.shuzi.pop()

    def pri0(self):
        print('.'.join(self.shuzi[:3]), ':'.join(self.shuzi[-3:]))

    def pri1(self):
        print('-'.join(self.shuzi[:3]), '-'.join(self.shuzi[-3:]))

    def pri2(self):
        print(''.join(self.shuzi[:3]), ''.join(self.shuzi[-3:]))


x = '2020年09月03日16时34分40秒'
a = Convdate(x)
a.pri0()
a.pri1()
a.pri2()
