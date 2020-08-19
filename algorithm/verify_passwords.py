# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/19 23:38
@ FileName     : verify_passwords.py
@ Description  : 验证密码
"""

flag = [0, 0, 0, 0]
psw = 'input()'
for i, v in enumerate(psw):
# for v in psw:
    if 3 <= i < len(psw)-3 :
        s = psw[i:i+3]
        if s in psw[0:i]:
            print('NG')
            break
    if sum(flag) >= 3:
        print('OK')
        break
    elif v.isdecimal():
        flag[0] = 1
    elif v.isupper():
        flag[1] = 1
    elif v.islower():
        flag[2] = 1
    else:
        flag[3] = 1
if sum(flag) >= 3:
    print('OK')
else:
    print('NG')
