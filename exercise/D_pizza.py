# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/18 21:21
# @FileName     : D_pizza.py
# @Software     : PyCharm
# --------------


# *toppings 创建了一个空的元组
def make_pizza(*toppings):
    """打印顾客所点的配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# 在函数定义中将接纳任意数量的实参的形参放在最后，先匹配位置实参和关键词实参，再将余下的实参都收集到最后一个形参中。
def make_pizza2(size, *toppings):
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

make_pizza2(16, 'pepperoni')
make_pizza2(14, 'mushroom', 'green peppers', 'extra cheese')
