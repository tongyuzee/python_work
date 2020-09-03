# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : curt.py
@ Date & Time   : 2020/7/21 14:34
@ Description   : 求立方根
"""

"""
在python2.7的doc中，round()的最后写着，"Values are rounded to the closest multiple of 10 to the power minus ndigits; 
if two multiples are equally close, rounding is done away from 0." 保留值将保留到离上一位更近的一端（四舍六入），如果距离两端一样远，
则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1。

但是到了python3.5的doc中，文档变成了"values are rounded to the closest multiple of 10 to the power minus ndigits; 
if two multiples are equally close, rounding is done toward the even choice." 如果距离两边一样远，会保留到偶数的一边。
比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。

简单的说就是，round(2.675, 2) 的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67。
为什么？这跟浮点数的精度有关。我们知道在机器中浮点数不一定能精确表达，因为换算成一串1和0后可能是无限位数的，机器已经做出了截断处理。
那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点，所以保留两位小数时就近似到了2.67。
"""


def curt(n):
    """求n的立方根"""
    i = 0.0001
    while i**3 < n:
        i += 0.04
    return i


x = float(input())
print("{:.1f}".format(curt(x)))
print("{}".format(curt(x)))

