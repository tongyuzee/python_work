# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/22 16:15
# @FileName     : python_repos.py
# @Software     : PyCharm
# --------------
import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print(response_dict.keys())
