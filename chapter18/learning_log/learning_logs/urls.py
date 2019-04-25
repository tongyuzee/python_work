# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/25 21:11
# @FileName     : urls.py
# @Software     : PyCharm
# --------------
"""定义learning——logs的模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index')
]

