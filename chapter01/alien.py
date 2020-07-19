#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author      :  tongyuze
@Project     :  chapter01
@File        :  alien.py
@Time        :  2020/4/28 21:40
@Description :  None
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 20
print(alien_0)

for key, value in alien_0.items():
    print('Key: ' + key)
    print('Value: ' + str(value) + '\n')

for key in alien_0.keys():
    print(key)

for v in alien_0.values():
    print(v)

x = {'a': 2, 'b': 2, 'd': 4, 'b': 4}    # Key值不能相同。出现相同的Key值，最后出现的Key-Value对将覆盖掉之前的。
print(x)
y = {'a', 'b', 'c', 'd', 'a'}
print(y)
z = set('I am a boy!')
print(z)
