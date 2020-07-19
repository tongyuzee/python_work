# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/3 0:00
# @FileName     : rw_visual.py
# @Software     : PyCharm
# --------------
import matplotlib.pyplot as plt

import random_walk

while True:

    rw = random_walk.RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.figure(dpi=128, figsize=(10, 6))
    # plt.scatter(rw.x_value, rw.y_value, c=point_numbers, s=5)
    plt.plot(rw.x_value, rw.y_value, linewidth=0.2)
    plt.scatter(0, 0, c='green', marker='^', s=10)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', marker='^', s=10)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another random walk? (y/n)\n")
    if keep_running == 'n':
        break
