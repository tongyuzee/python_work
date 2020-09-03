# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/7/25 11:08
@ FileName     : Redraiment.py
@ Description  :
                题目描述
                Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，但走的步数最多，不知道为什么？
                你能替Redraiment研究他最多走的步数吗？

                样例输入
                6
                2 5 1 5 4 5

                样例输出
                3

                提示
                Example:
                6个点的高度各为 2 5 1 5 4 5；如从第1格开始走,最多为3步, 2 4 5；从第2格开始走,最多只有1步,5；
                而从第3格开始走最多有3步,1 4 5；从第5格开始走最多有2步,4 5；所以这个结果是3。
"""

n = int(input())
xin = [int(i) for i in input().split()]

dp = [1] * n        # dp[i] 表示以第i个桩结尾时，最多走的步数。默认为1
for i in range(1, n):
    for j in range(i):
        if xin[j] < xin[i]:
            """
            如果第i个桩之前存在比它矮的第j个桩，那么可以从第j个桩走到第i个桩，此时，通过j走到i的最多的步数为dp[j]+1;
            遍历所有的j, 所对应的（dp[j]+1）中的最大值便是dp[i](以第i个桩结尾时，最多走的步数)。
            """
            dp[i] = max(dp[i], dp[j]+1)
res = max(dp)
print(res)
