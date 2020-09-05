# -*- coding: utf-8 -*-
"""
@ Author        : tongyuze
@ Project       : Fluent_Py
@ Date & Time   : 2020/9/5 18:57
@ FileName      : 2.9array.py
@ Description   : 数组array
"""
import array

floats = array.array('d', [1, 2, 3, 4])
print(list(floats))
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array.array('d')
fp = open("floats.bin", 'rb')
floats2.fromfile(fp, 4)
print(list(floats2))
