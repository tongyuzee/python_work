# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/23 21:09
# @FileName     : remember_me.py
# @Software     : PyCharm
# --------------

import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We will remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
