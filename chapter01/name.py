#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  name.py
@Time        :  2020/4/14 23:29
@Description :  None
"""

name = 'ada lovelace'
# 方法
print(name.title())  # 首字母大写
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写

print('')       # print语句默认在末尾输出一个换行符号

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
