# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/31 21:56
# @FileName     : test_survey.py
# @Software     : PyCharm
# --------------
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试"""

    def test_store_signal_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Spanish']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


# if __name__ == '__main__':
#     unittest
unittest.main()
