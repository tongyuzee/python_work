# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/20 22:26
# @FileName     : my_cars.py
# @Software     : PyCharm
# --------------
# 导入多个类
# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', '2016')
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'model s', '2016')
# print(my_tesla.get_descriptive_name())

# 导入整个模块
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())




