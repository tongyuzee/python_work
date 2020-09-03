# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/21 15:10
@ FileName     : sort_merge.py
@ Description  : 归并排序
"""


def merge(left, right):
    # 如果有一个数组为空，那么不需要合并，
    # 可以直接将另一个数组返回作为结果
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    i_left, i_right = 0, 0
    # 查看两个数组直到所有元素都装进结果数组中
    while len(result) <= len(left) + len(right):
        if left[i_left] < right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1

        # 如果哪个数组达到了最后一个元素，那么可以将另外一个数组的剩余元素
        # 装进结果列表中，然后终止循环
        if i_left >= len(left):
            result += right[i_right:]
            break
        if i_right >= len(right):
            result += left[i_left:]
            break
    return result


def merge_sort(arry):
    # 如果输入数组包含元素不超过两个，那么返回它作为函数结果
    if len(arry) < 2:
        return arry

    midpoint = len(arry) // 2

    # 对数组递归地划分为两部分，排序每部分然后合并装进最终结果列表
    return merge(merge_sort(arry[:midpoint]), merge_sort(arry[midpoint:]))


a = [8, 6, -4]
r = merge_sort(a[:])
print(' '.join([str(_) for _ in r]))
