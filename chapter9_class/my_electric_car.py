# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/20 22:21
# @FileName     : my_electric_car.py
# @Software     : PyCharm
# --------------
# from car import ElectricCar
#
# my_tesla = ElectricCar('tesla', 'model s', '2016')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

from electric_car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(300)
my_tesla.read_odometer()
my_tesla.increment_odometer(36)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()


