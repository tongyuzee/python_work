# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/1 0:00
# @FileName     : mpl_squares.py
# @Software     : PyCharm
# --------------
import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(values, squares, linewidth=3)

plt.title('Square Numbers', fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
