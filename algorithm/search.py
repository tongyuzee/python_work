# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/24 21:53
@ FileName     : search.py
@ Description  : 二分查找（bisect）
"""
import bisect

# h 必须为有序数组
haystack = [1, 4, 5, 6, 8, 10, 15, 17, 18, 19, 25, 30, 31]
needles = [0, 1, 24, 30, 5, 8, 58, 32, 6, 17]


b = input("Enter 'l' or 'r:").lower()
if b == 'l':
    bisect_fn = bisect.bisect_left
else:
    bisect_fn = bisect.bisect_right

print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('{:2d}'.format(n) for n in needles))

row_fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'
for n in sorted(needles, reverse=True):
    position = bisect_fn(haystack, n)
    offset = '  |' * position
    print(row_fmt.format(n, position, offset))
