# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/22 23:39
# @FileName     : word_count.py
# @Software     : PyCharm
# --------------


def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file '" + filename + "' does not exist.")
    else:
        words = contents.split()
        print("The file '" + filename + "' has about " + str(len(words)) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for f_name in filenames:
    count_words(f_name)
