# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/17 20:57
# @FileName     : greeter.py
# @Software     : PyCharm
# --------------


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


greet_user('jesse')
# 位置实参，实参的顺序与形参的顺序必须相同。
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# 关键字实参，传递给函数 名称-值 对，顺序无关紧要。
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
