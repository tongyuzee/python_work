# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/31 20:56
# @FileName     : survey.py
# @Software     : PyCharm
# --------------


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷的答案"""
        self.responses.append(new_response)

    def show_result(self):
        """"""
        print("Survey results:")
        for response in self.responses:
            print("-" + response)
