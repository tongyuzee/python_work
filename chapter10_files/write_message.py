# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/21 21:51
# @FileName     : write_message.py
# @Software     : PyCharm
# --------------

filename = 'programming.txt'
# 以写入模式打开文件。如果文件不存在，则创建文件；否则，先清空该文件再写入信息。
with open(filename, 'w') as file_obj:
    file_obj.write("I love programming.\n")
    file_obj.write("I love creating new games.\n")

# 以附加模式打开文件。再文件末尾添加内容，而不是覆盖原来的内容。
with open(filename, 'a') as file_obj:
    file_obj.write("I also love finding meaning in large datasets.\n")
