# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/20 22:46
# @FileName     : favorite_languages.py
# @Software     : PyCharm
# --------------
# 从模块collections中导入OrderedDict类
# OrderedDict类和字典的区别只在于记录了键值对添加的顺序
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

