# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/18 8:33
# @FileName     : b_person.py
# @Software     : PyCharm
# --------------


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
        person['age'] = int(age)
    return person


musician = build_person('jimi', 'hendrix', age='27')
print(musician)
