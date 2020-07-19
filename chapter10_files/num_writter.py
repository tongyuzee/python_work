# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/23 0:09
# @FileName     : num_writter.py
# @Software     : PyCharm
# --------------
import json

num = [2, 3, 4, 5, 6, 7]

filename = 'num.json'
with open(filename, 'w') as f_obj:
    json.dump(num, f_obj)
