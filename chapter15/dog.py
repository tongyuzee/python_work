# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2020/7/9 20:12
# @FileName     : dog.py
# @Software     : PyCharm
# --------------


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + ' rolled over.')


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is {!s} years old.".format(my_dog.age))
my_dog.sit()
my_dog.roll_over()
