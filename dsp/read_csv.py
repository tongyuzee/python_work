# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/15 13:23
# @FileName     : read_csv.py
# @Software     : PyCharm
# --------------

import csv


def csvread(filename, start=0):
    with open(filename, 'r') as fl:
        reader = csv.reader(fl)
        sig = list(reader)
        sig_x = [[float(x) for x in y] for y in sig[start:]]
        return sig_x


dat1 = csvread("sig.dat")
dat2 = csvread("5678EDBC.dat", 1)
