# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/19 12:40
# @FileName     : pizza.py
# @Software     : PyCharm
# --------------


def make_pizza(size, *toppings):
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
