# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/26 21:44
@ FileName     : zuichanghuiwenzichuan.py
@ Description  : 最长回文子串
"""

s = input()
n = len(s)
dp, ans = [[False] * n for _ in range(n)], ''
for l in range(n):
    for i in range(n):
        j = i + l
        if j >= n:
            break
        else:
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

        # 只有当 ans 比 s[i:j+1] 短时，才更新 ans
        if dp[i][j] and len(ans) < l+1:
            ans = s[i:j+1]
print(ans)
