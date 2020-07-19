# -*- coding: utf-8 -*-
# @Author       :tongyuze
# @Date & Time  : 2019/3/17 15:38
# @FileName     : mountain_poll.py
# @Software     : PyCharm
# --------------

responses = {}

while True:
    name = input("What's your name?\n")
    response = input("Which mountain would you like to climb someday?\n")
    responses[name] = response
    repeat = input("Would you like to another person respond? (yes/no)\n")
    if repeat.lower() == 'no':
        break

print("\n----- Poll Results -----")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
