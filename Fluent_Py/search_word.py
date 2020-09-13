# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : Fluent_Py
@ Date & Time   : 2020/9/13 21:41
@ FileName      : search_word.py
@ Description   : None
"""
from typing import List


def exist(b: List[List[str]], w: str) -> bool:
    m = len(b)
    n = len(b[0])
    if m == 0 or n == 0:
        return False
    mark = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if b[i][j] == w[0]:
                mark[i][j] = 1
                if backtrack(i, j, mark, b, w[1:]):
                    return True
                else:
                    mark[i][j] = 0
    return False


def backtrack(i, j, mark, b, w):
    m = len(b)
    n = len(b[0])
    if len(w) == 0:
        return True
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for cur_d in directions:
        cur_i, cur_j = cur_d
        cur_i += i
        cur_j += j
        if 0 <= cur_i < m and 0 <= cur_j < n and b[cur_i][cur_j] == w[0]:
            if mark[cur_i][cur_j] == 1:
                continue
            mark[cur_i][cur_j] = 1
            if backtrack(cur_i, cur_j, mark, b, w[1:]):
                return True
            else:
                mark[cur_i][cur_j] = 0
    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'SES'
print(exist(board, word))
