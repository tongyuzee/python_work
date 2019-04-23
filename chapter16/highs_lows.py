# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/7 22:29
# @FileName     : highs_lows.py
# @Software     : PyCharm
# --------------
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)   # 逗号隔开的每一项数据作为一个元素存储在列表中
    # print(header_row)

    # 对列表调用enumerate()获取每个元素的索引与位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs = [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
        highs.append(int(row[1]))

    # print(highs)

fig = plt.figure(1, dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title("Daily high temperatures, 2014", fontsize=16)
plt.xlabel("Date", fontsize=12)
fig.autofmt_xdate()     # 绘制斜的日期标签
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()
