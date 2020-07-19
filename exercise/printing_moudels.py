# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/18 12:49
# @FileName     : printing_moudels.py
# @Software     : PyCharm
# --------------


def print_models(unprinted_designs, cpl_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中
    :param unprinted_designs:
    :param cpl_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        cpl_models.append(current_design)


def show_completed_models(cpl_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in cpl_models:
        print(completed_model)


unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 在函数中对列表做的任何修改都是永久性地。
print_models(unprinted_models, completed_models)

# 切片表示法[:]创建列表的副本，函数只会修改副本，而不影响原件。
print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print(unprinted_models)
