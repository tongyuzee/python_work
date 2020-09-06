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
    for ii, v in enumerate(dp):
        if z in v:
            zz.append(ii)
    return zz


m, n = input().split()
a = []
for j in range(int(n)):
    a.append(input().split()[1:])
b = ['0']
c = []
i = 0
while True:
    if i >= len(b):
        break
    x = find(a[:], b[i])
    for u in x:
        if u not in c:
            c.append(u)
            for uu in a[u]:
                if uu not in b:
                    b.append(uu)
    i = i + 1
print(len(b))
