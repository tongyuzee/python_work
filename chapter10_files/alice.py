# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/22 12:37
# @FileName     : alice.py
# @Software     : PyCharm
# --------------
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file '" + filename + "' does not exist.")
else:
    words = contents.split()
    print("The file '" + filename + "' has about " + str(len(words)) + " words.")
