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
    # bisect_left 返回的插入位置是原序列中和被插入元素相等的元素的位置，即新元素被放在与它相等的元素之前
    bisect_fn = bisect.bisect_left
    bisect_in = bisect.insort_left
else:
    # bisect.bisect = bisect.bisect_right
    # bisect_right 返回的插入位置是原序列中和被插入元素相等的元素之后的位置，即新元素被放在与它相等的元素之后
    bisect_fn = bisect.bisect_right
    bisect_in = bisect.insort_right

print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('{:2d}'.format(h) for h in haystack))
row_fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'
for n in sorted(needles, reverse=True):
    position = bisect_fn(haystack, n)
    offset = '  |' * position
    print(row_fmt.format(n, position, offset))

print('DEMO:', bisect_in.__name__)
for n in needles:
    bisect_in(haystack, n)
    print("{:2d}".format(n), haystack)
