#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  birthday.py
@Time        :  2020/4/15 14:06
@Description :  None
"""

age = 23
message = "Happy " + str(age) + "rd birthday!"
print(message)

message1 = " best wishes "
print(message1)
print(message1.rstrip())        # 删除末尾空格
print(message1.lstrip())        # 删除开头空格
print(message1.strip())         # 删除两端空格
