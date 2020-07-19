# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/2 12:18
# @FileName     : scatter_squares.py
# @Software     : PyCharm
# --------------
import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]   # 列表解析

plt.figure(1)
plt.scatter(x_value, y_value, c=[(0, 0.7, 0)], s=10)
plt.title("Square Numbers", fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('Squares_plot.png', bbox_inches='tight')
plt.figure(2)
plt.plot(x_value, y_value)

plt.show()
