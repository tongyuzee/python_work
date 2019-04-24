# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/24 11:13
# @FileName     : py_repos.py
# @Software     : PyCharm
# --------------
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# 将API响应（JOSN格式）转换为字典
response_dict = r.json()

# 处理结果
# print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 20
my_style.label_font_size = 10
my_style.major_label_font_size = 14

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title = u"Most-Starred Python Projects on GitHub"
my_config.range = (0, 70000)
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.x_labels = names
chart.add('python', stars)
chart.render_to_file('py_repos.svg')
