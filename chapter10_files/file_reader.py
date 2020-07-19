# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/21 12:56
# @FileName     : file_reader.py
# @Software     : PyCharm
# --------------

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 以绝对字符串的方式指定文件路径
file_path = r'e:\WorkSpace\Python_work\chapter10_files\pi_digits.txt'
with open(file_path) as f_obj:
    print(f_obj.read())

    for line in f_obj:
        print(line)

    lines = f_obj.readlines()

for line in lines:
    print(line)
