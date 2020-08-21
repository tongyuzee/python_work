# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/17 23:00
@ FileName     : sort_maopo.py
@ Description  : 冒泡排序
"""

# a = [int(_) for _ in input().split()]
a = [2, 9, 4, 5, 6]
for i in range(len(a)):
    flag = 1        # falg 表示最后一轮是否有交换位置
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            flag = 0        # 如果有交换位置， flag = 0
    if flag:        # flag = 1 表示没有交换位置，说明已经排序完成，无需再进行排序，退出循环。
        break
print(' '.join([str(_) for _ in a]))
