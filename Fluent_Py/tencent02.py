# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : Fluent_Py
@ Date & Time   : 2020/9/6 20:14
@ FileName      : tencent02.py
@ Description   : None
"""


def find(dp, z):
    zz = []
    for v in dp:
        if z in v:
            zz += v
    return list(set(zz))


m, n = input().split()
a = []
for i in range(int(n)):
    a.append(input().split()[1:])
print(a)
b = ['0']
i = 0
while True:
    if i >= len(b):
        break
    x = find(a[:], b[i])
    i = i + 1
    if not x:
        b += x
        b = list(set(b))

print(b)
