# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/20 22:35
# @FileName     : electric_car.py
# @Software     : PyCharm
# --------------
from car import Car


class Battery:
    """模拟一次电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print("This electric car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()    # 创建一个新的Battery实例，并将其存储在属性self.battery中
