# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/25 21:20
# @FileName     : testname.py
# @Software     : PyCharm
# --------------
import unittest
from formattedname import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试formatted_name.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
