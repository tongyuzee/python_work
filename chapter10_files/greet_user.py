# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/23 21:14
# @FileName     : greet_user.py
# @Software     : PyCharm
# --------------
import json

filename = 'username.json'

with open(filename, 'r') as f_obj:
    username = json.load(f_obj)

print("Welcome back, " + username + "!")
