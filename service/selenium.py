#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/20 9:36
# @Author : ActStrady@tom.com
# @FileName : selenium.py
# @GitHub : https://github.com/ActStrady/selenium-learn

"""
selenium 的常用操作
"""

from selenium import webdriver

# 获取驱动
driver = webdriver.Chrome()
# 执行请求
driver.get('https://movie.douban.com/')
# 获取页面所有信息
HTML = driver.page_source
print(HTML)
# 查找结点
