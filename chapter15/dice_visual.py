# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/3 21:46
# @FileName     : dice_visual.py
# @Software     : PyCharm
# --------------
import pygal
import die

die_1 = die.Die()
die_2 = die.Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for value in range(2, die_1.num_side + die_2.num_side + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.HorizontalBar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_title = "Results"
hist.y_title = "Frequency of Results"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

hist.add("D6+D6", frequencies)
hist.render_to_file('dice_visual.svg')
