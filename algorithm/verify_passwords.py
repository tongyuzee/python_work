# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/19 23:38
@ FileName     : verify_passwords.py
@ Description  : 验证密码
"""


def verify(psw):
    if len(psw) <= 8:
        return 'NG'
    flag = [0, 0, 0, 0]
    for i, v in enumerate(psw):
        if 3 <= i <= len(psw) - 3:
            s = psw[i:i + 3]
            t = psw[:i]
            if s in t:
                return 'NG'
        if v.isdecimal():
            flag[0] = 1
        elif v.isupper():
            flag[1] = 1
        elif v.islower():
            flag[2] = 1
        else:
            flag[3] = 1
    if sum(flag) >= 3:
        return 'OK'
    else:
        return 'NG'


p = '0Aw&50Aw2'
print(verify(p))
