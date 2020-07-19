# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/23 0:18
# @FileName     : num_reader.py
# @Software     : PyCharm
# --------------
import json

filename = 'num.json'
with open(filename, 'r') as f_obj:
    num = json.load(f_obj)

print(num)
