# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/25 21:02
# @FileName     : name.py
# @Software     : PyCharm
# --------------

from formattedname import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
