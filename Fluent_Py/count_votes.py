# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : count_votes.py
@ Date & Time   : 2020/7/31 16:23
@ Description   : 统计选票
"""

"""必须按照输入候选人的顺序输出选票数量"""

n, candidate = int(input()), input().strip().split()
m, vote = int(input()), input().strip().split()

valid = 0
for c in candidate:
    if c in vote:
        valid += vote.count(c)
    print('{} : {}'.format(c, vote.count(c)))
print("Invalid : {}".format(m - valid))
