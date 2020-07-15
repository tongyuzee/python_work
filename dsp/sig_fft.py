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
plt.figure(1)
plt.plot(t, xt)

nf = 1024
f = np.linspace(0, fs, nf, endpoint=False)
xf = fft(xt, nf)
# 取绝对值并归一化
xfa = np.abs(xf)/np.amax(np.abs(xf))
plt.figure(2)
plt.plot(f[0:nf//2], xfa[0:nf//2])
plt.show()

f_out = np.argmax(xfa[0:nf//2])/nf*fs
print("信号频率为：{:.2f}Hz".format(f_out))
