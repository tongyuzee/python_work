# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/17 22:48
# @FileName     : pets.py
# @Software     : PyCharm
# --------------


# 可以指定形参的默认值,指定默认值的形参放在最后
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 调用函数时可以省略有默认值的形参，此时形参为默认值。
describe_pet(pet_name='willie')
# 位置实参
describe_pet('willie')
# 当给有默认值的形参提供了实参时，将忽略这个形参的默认值。
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('harry', 'hamster')
