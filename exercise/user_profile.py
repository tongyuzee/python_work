# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/18 22:05
# @FileName     : user_profile.py
# @Software     : PyCharm
# --------------


# **user_info 创建了一个空的字典，并将收到的所有“名称-值”对封装到这个字典中。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    pass
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='Princetion', field='physics')
print(user_profile)
