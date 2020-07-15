# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/15 13:23
# @FileName     : read_csv.py
# @Software     : PyCharm
# --------------

import csv


def csvread(filename, row=0, column=0):
    """从文件filename的第row行第column列开始读取数据，默认均为0"""

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        sig = list(reader)
        sig_x = [[float(x) for x in y[column:]] for y in sig[row:]]
        return sig_x


dat1 = csvread("sig.dat")
dat2 = csvread("5678EDBC.dat", 1, 0)
