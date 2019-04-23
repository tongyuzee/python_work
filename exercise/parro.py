# -*- coding: utf-8 -*
# -------------------
# Author: tongyuze
# Date: 2019.03.17
# -------------------

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"

# 方法一
# message = ''
# while message.lower() != 'quit':
#     message = input(prompt)
#     if message.lower() != 'quit':
#         print(message)

# 方法二：使用标志
# active = True
# while active:
#     message = input(prompt)
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)

# 方法三：使用break语句
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
