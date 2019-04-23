# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/22 16:15
# @FileName     : python_repos.py
# @Software     : PyCharm
# --------------
import requests

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
# 研究第一个仓库（repositoriy）
repo_1 = repo_dicts[0]
# print("\nKeys:", len(repo_1))
# for key in sorted(repo_1.keys()):
#     print(key)
print("\nSelected information about first repositories:")
print("Name:", repo_1['name'])
print("Owner:", repo_1['owner']['login'])
print("Stars:", repo_1['stargazers_count'])
print("Repository:", repo_1['html_url'])
print("Created at:", repo_1['created_at'])
print("Updated at:", repo_1['updated_at'])
print("Description:", repo_1['description'])
