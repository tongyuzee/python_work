# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/20 20:59
# @FileName     : my_car.py
# @Software     : PyCharm
# --------------
# 导入单个类
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

