# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : cards.py
@ Date & Time   : 2020/8/1 15:28
@ Description   : None
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        """私有属性"""
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()
# 通过 特殊（magic）方法 __len__() 实现
print(len(deck))
# 通过 特殊（magic）方法 __getitem__() 实现
print(deck[0])
print(deck[-1])
print(deck[2::13])
print(choice(deck))

for card in deck:
    print(card)
