# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/13 11:46
# @FileName     : sig_fft.py
# @Software     : PyCharm
# --------------
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

fs = 4000
tp = 2
t = np.linspace(0, tp, tp * fs, endpoint=False)
xt = np.cos(2*np.pi*200*t)
plt.subplot(1, 2, 1)
plt.plot(t, xt)

nf = 1024
f = np.linspace(0, fs, nf, endpoint=False)
xf = fft(xt, nf)
plt.subplot(1, 2, 2)
plt.plot(f, abs(xf))
plt.show()
pass
