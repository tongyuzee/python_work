# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/14 18:29
# @FileName     : sig_fft.py
# @Software     : PyCharm
# --------------

import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

Fs = 10000
Tp = 2
t = np.linspace(0, Tp, Tp * Fs, endpoint=False)
xt = np.cos(2 * np.pi * 450 * t)
plt.figure(1)
plt.plot(t, xt)

NF = 4096
f = np.linspace(0, Fs, NF, endpoint=False)
xf = fft(xt, NF)
xaf = np.abs(xf)/np.amax(np.abs(xf))
plt.figure(2)
plt.plot(f[0:NF//2], xaf[0:NF//2])
plt.show()

f1 = np.argmax(xaf)/NF*Fs
f2 = np.where(xaf[0:NF//2] == 1)
print("信号频率为：{:.2f}".format(f1))
print("信号频率为：{:.2f}".format(f2[0][0]/NF*Fs))
