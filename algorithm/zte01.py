# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/27 10:29
@ FileName     : zte01.py
@ Description  : None
"""

m, n = [int(_) for _ in input().split()]
A, ans = [], 0
for i in range(m):
    A.append([int(_) for _ in input().split()])
    if i >= 2:
        for j in range(1, n - 1):
            res = A[i-1][j-1] + A[i-1][j] + A[i-1][j+1] + A[i-2][j] + A[i][j]
            if res > ans:
                ans = res
# ans = 0
# for i in range(1, m-1):
#     for j in range(1, n-1):
#         res = sum([A[i][j], A[i-1][j], A[i+1][j], A[i][j-1], A[i][j+1]])
#         if res > ans:
#             ans = res
print(ans)
