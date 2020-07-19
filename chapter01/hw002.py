#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  hw002.py
@Time        :  2020/4/22 19:18
@Description :  None
"""

x = input('')
x.strip()
# xl = x.split('5a ')
xl = x.split()
print(xl)

ps = []
p = []
for v in xl:
    if v == '5a':
        ps.append(p)
        p = []
    else:
        p.append(v)
while [] in ps:
    ps.remove([])
# print(ps)

cp = []
for i in range(len(ps)):

    flag = 0
    z = ps[i][:]
    while '5b' in z:
        w = z.index('5b')
        if z[w + 1] != 'bb' and z[w + 1] != 'ba':
            flag = 1
        z.remove('5b')

    sn = ''.join(ps[i])
    if '5a' in sn or flag == 1:
        continue
    else:
        n = int(ps[i][-1], 16)
        if '5bba' in sn:
            n = n + 1
        if '5bbb' in sn:
            n = n + 1
        if len(ps[i]) == n + 1:
            cp.append(ps[i])
# print(cp)

y = []
for i in range(len(cp)):
    cp[i].insert(0, '5a')
    y.append(' '.join(cp[i]))
y.append('5a')
print(' '.join(y))
