# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/12 21:54
# @FileName     : sig_fft.py
# @Software     : PyCharm
# --------------

import numpy as np
# from sci
import matplotlib.pyplot as plt

fs = 4000
tp = 2
t = np.linspace(0, tp, tp * fs, endpoint=False)

xt = np.cos(2*np.pi*200*t)
plt.plot(t, xt)
plt.show()
