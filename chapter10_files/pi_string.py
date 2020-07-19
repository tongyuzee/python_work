# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/21 20:12
# @FileName     : pi_string.py
# @Software     : PyCharm
# --------------

file_path = r'e:\WorkSpace\Python_work\chapter10_files\pi_million_digits.txt'
with open(file_path) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52])
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy:\n")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi!")
