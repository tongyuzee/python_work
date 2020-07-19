# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/17 23:41
# @FileName     : formatted_name.py
# @Software     : PyCharm
# --------------


# 指定middle_name默认值为“空字符串”，使其相应的实参变成可选的。
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:     # 非空字符串解读为True
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

while True:
    print("\nPlease tell me your name.")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name.title())
