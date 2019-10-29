#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019-10-12 13:42
# @Author : jared
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render_to_response

def home(request):
    context = {}
    return render_to_response('home.html',context)