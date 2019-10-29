#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019-10-12 10:20
# @Author : jared
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/blog/1
    path('<int:blog_pk>/',views.blog_detail,name='blog_detail'),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name='blogs_with_type'),
    path('',views.blog_list,name='blog_list'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name="blogs_with_date")
]