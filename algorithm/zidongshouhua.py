# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : zidongshouhua.py
@ Date & Time   : 2020/7/28 15:19
@ Description   : 自动售货机
"""


class Store:
    """自动收货系统"""

    def __init__(self, a1=0, a2=0, a3=0, a4=0, a5=0, a6=0, y1=0, y2=0, y5=0, y10=0):
        """初始化, 输入参数为整数（int）"""
        self.goods = {'A1': [2, a1], 'A2': [3, a2], 'A3': [4, a3], 'A4': [5, a4], 'A5': [8, a5], 'A6': [6, a6]}
        self.money = {'1': y1, '2': y2, '5': y5, '10': y10}
        self.change = 0

    def reset(self, a, y):
        """重置系统, 输入参数为整数列表"""

        self.goods = {'A1': [2, a[0]], 'A2': [3, a[1]], 'A3': [4, a[2]], 'A4': [5, a[3]], 'A5': [8, a[4]], 'A6': [6, a[5]]}
        self.money = {'1': y[0], '2': y[1], '5': y[2], '10': y[3]}
        print("S001:Initialization is successful")

    def sum_m(self, coins):
        """计算存钱盒总额, 输入参数为字符串列表"""
        s = 0
        for c in coins:
            s += self.money[c] * int(c)
        return s

    def sum_g(self):
        """计算商品总数"""
        s = 0
        for c in self.money.values():
            s += c
        return s

    def coin(self, m):
        """投币, 输入参数为字符串"""
        if m not in self.money.keys():
            print("E002:Denomination error")
        elif m not in ['1', '2'] and self.sum_m(['1', '2']) < int(m):
            print("E003:Change is not enough, pay fail")
        elif int(m) + self.change > 10:
            print("E004:Pay the balance is beyond the scope biggest")
        elif self.sum_g() == 0:
            print("E005:All the goods sold out")
        else:
            self.change += int(m)
            self.money[m] += 1
            print("S002:Pay success,balance=" + str(self.change))

    def search(self, m):
        """查询, 输入参数为字符串"""
        if m not in ['0', '1']:
            print("E010:Parameter error")
        elif m == '0':
            g = {}
            for gk, gv in self.goods.items():
                if gv[-1] not in g.keys():
                    g[gv[-1]] = [gk]
                else:
                    g[gv[-1]].append(gk)
            for ci in sorted(g.keys()):
                for cj in sorted(g[ci]):
                    print("{} {} {}".format(cj, self.goods[cj][0], self.goods[cj][-1]))
        else:
            for mk, mv in self.money.items():
                print("{} yuan coin number={}".format(mk, mv))


x = Store()

cmds = input().split(';')
while '' in cmds:
    cmds.remove('')

for cmd in cmds:
    if cmd[0] == 'r':
        nums = cmd[2:].split(' ')
        goods = [int(v) for v in nums[0].split('-')]
        money = [int(v) for v in nums[1].split('-')]
        x.reset(goods, money)
    elif cmd[0] == 'p':
        x.coin(cmd[2:])
    elif cmd[0] == 'q':
        x.search(cmd[2:])
