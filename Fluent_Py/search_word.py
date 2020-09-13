# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : Fluent_Py
@ Date & Time   : 2020/9/13 21:41
@ FileName      : search_word.py
@ Description   : None
"""


def find(b, s):
    pp = []
    for ii, bb in enumerate(b):
        if s in bb:
            for jj, bbb in enumerate(bb):
                if bbb == s:
                    pp.append((ii, jj))
    return pp


def around(b, pp):
    ar = {}
    ii, jj = pp
    m = len(b)
    n = len(b[0])
    if ii - 1 >= 0:
        ar[b[ii - 1][jj]] = (ii - 1, jj)
    if jj - 1 >= 0:
        ar[b[ii][jj-1]] = (ii, jj - 1)
    if ii + 1 < m:
        ar[(ii+1, jj)] = b[ii+1][jj]
    if jj + 1 < n:
        ar[(ii, jj+1)] = b[ii][jj+1]
    return ar


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'SEE'
for i in range(len(word)):
    p = find(board, word[i])
    if p:
        for v in p:
            a = around(board, v)
    else:
        break
