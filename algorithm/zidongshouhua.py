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
        self.ch_n = {'1': 0, '2': 0, '5': 0, '10': 0}
        self.balance = 0

    def reset(self, a, y):
        """重置系统, 输入参数为整数列表"""

        for gk in self.goods.keys():
            self.goods[gk][-1] = a[int(gk[-1]) - 1]
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
        for c in self.goods.values():
            s += c[-1]
        return s

    def coin(self, m):
        """投币, 输入参数为字符串"""
        if m not in self.money.keys():
            print("E002:Denomination error")
        elif m not in ['1', '2'] and self.sum_m(['1', '2']) < int(m):
            print("E003:Change is not enough, pay fail")
        elif int(m) + self.balance > 10:
            print("E004:Pay the balance is beyond the scope biggest")
        elif self.sum_g() == 0:
            print("E005:All the goods sold out")
        else:
            self.balance += int(m)
            self.money[m] += 1
            print("S002:Pay success,balance=" + str(self.balance))

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
            for ci in sorted(g.keys(), reverse=True):
                for cj in sorted(g[ci]):
                    print("{} {} {}".format(cj, self.goods[cj][0], self.goods[cj][-1]))
        else:
            for mk, mv in self.money.items():
                print("{} yuan coin number={}".format(mk, mv))

    def buy(self, m):
        """购买商品，输入参数为字符串"""
        if m not in self.goods.keys():
            print("E006:Goods does not exist")
        elif self.goods[m][-1] == 0:
            print("E007:The goods sold out")
        elif self.balance < self.goods[m][0]:
            print("E008:Lack of balance")
        else:
            self.goods[m][-1] -= 1  # 商品数量-1
            self.balance -= self.goods[m][0]  # 余额减商品价格
            print("S003:Buy success,balance=" + str(self.balance))

    def change(self):
        """找零"""
        if self.balance == 0:
            print("E009:Work failure")
        else:
            for mk in ['10', '5', '2', '1']:
                while self.balance >= int(mk) and self.money[mk] != 0:
                    self.balance -= int(mk)
                    self.ch_n[mk] += 1
                    self.money[mk] -= 1
            for ck, cv in self.ch_n.items():
                print("{} yuan coin number={}".format(ck, cv))
            """退币完成，清零"""
            self.balance = 0
            self.ch_n = {'1': 0, '2': 0, '5': 0, '10': 0}


x = Store()
while True:
    command = input("\nEnter 'q' or 'Q' to quit.\n")
    if command.lower() == 'q':
        break
    else:
        cmds = command.split(';')
        while '' in cmds:
            cmds.remove('')
        for cmd in cmds:
            if cmd[0] == 'r':
                nums = cmd[2:].split(' ')
                goods = [int(v) for v in nums[0].split('-')]
                money = [int(v) for v in nums[1].split('-')]
                x.reset(goods[:], money[:])
            elif cmd[0] == 'p':
                x.coin(cmd[2:])
            elif cmd[0] == 'q':
                x.search(cmd[2:])
            elif cmd[0] == 'b':
                x.buy(cmd[2:])
            elif cmd[0] == 'c':
                x.change()
            else:
                break
