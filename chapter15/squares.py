# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/1 21:29
# @FileName     : squares.py
# @Software     : PyCharm
# --------------
import matplotlib.pyplot as plt

x_value = list(range(-100, 101))
y_value = [x**2 for x in x_value]
# cc = [[0, 0, 0.8]]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=5)
plt.show()
