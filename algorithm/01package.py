# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : 01package.py
@ Date & Time   : 2020/8/12 17:50
@ Description   : 01背包
"""

# n为商品数量， m为背包总容量
n, m = 6, 12
v = [0, 8, 10, 6, 3, 7, 2]      # 价值数组
w = [0, 4, 6, 2, 2, 5, 1]       # 重量数组

"""
创建二维数组
*-------------
f = [[0] * (m + 1)] * (n + 1)
*-------------
list * n—>n shallow copies of list concatenated
n个list的浅拷贝的连接
相当于创建了numRows个相同的指向array的指针，每次修改其中一个指针之后，所有的指针都会被修改！！！！！
修改其中的任何一个元素会改变整个列表
"""
f = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= w[i]:
            f[i][j] = max(f[i-1][j], f[i-1][j-w[i]] + v[i])
        else:
            f[i][j] = f[i-1][j]

"""寻找二维数组的最大值及其坐标"""
temp, m_j, m_i = 0, 0, 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if f[i][j] > temp:
            temp = f[i][j]
            m_i = i
            m_j = j

"""
m[n][c]为最优值，如果m[n][c]=m[n-1][c] ,说明有没有第n件物品都一样，则x[n]=0 ; 否则 x[n]=1。
当x[n]=0时，由x[n-1][c]继续构造最优解；当x[n]=1时，则由x[n-1][c-w[i]]继续构造最优解。
"""
x = [0] * n
for i in range(m_i-1, -1, -1):
    if f[i][m_j] != f[i-1][m_j]:
        x[i] = 1
        m_j -= w[i]
