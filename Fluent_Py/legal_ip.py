# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : legal_ip.py
@ Date & Time   : 2020/8/13 16:59
@ Description   : 合法IP
"""


def islegal(ip):
    """判断ipv4的IP是否合法"""
    x = ip.split('.')
    if len(x) != 4:
        return 'NO'
    else:
        for v in x:
            if not v.isdecimal() or int(v) > 255:
                return 'NO'
        return 'YES'


print(islegal(input()))
