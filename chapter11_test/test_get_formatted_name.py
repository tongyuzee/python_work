# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/25 23:07
# @FileName     : test_get_formatted_name.py
# @Software     : PyCharm
# --------------
from unittest import TestCase
from name_function import get_formatted_name


class TestGetformattedname(TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
