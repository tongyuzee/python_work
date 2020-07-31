# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : count_votes.py
@ Date & Time   : 2020/7/31 16:23
@ Description   : 统计选票
"""

n, candidate = int(input()), input().strip().split()

votes = {'Invalid': 0}
for i in candidate:
    votes[i] = 0

m, v = int(input()), input().strip().split()
for i in v:
    if i in votes.keys():
        votes[i] += 1
    else:
        votes['Invalid'] += 1

for k in sorted(votes.keys()):
    if k != 'Invalid':
        print("{} : {}".format(k, votes[k]))
print("Invalid : {}".format(votes['Invalid']))
