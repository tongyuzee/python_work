# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/19 12:25
# @FileName     : making_pizza.py
# @Software     : PyCharm
# --------------

# 导入整个模块
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
# import pizza as p
#
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, "mushroom", 'green peppers', 'extra cheese')

# 导入模块中的特定函数
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# 使用as给函数指定别名
# from pizza import make_pizza as mp
#
# mp(16, 'pepperoni')
# mp(12, 'mushroom', 'green peppers', 'extra cheese')

# 导入模块中的所欲函数
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
