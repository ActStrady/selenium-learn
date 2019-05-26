#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/20 9:36
# @Author : ActStrady@tom.com
# @FileName : get_boss_java.py
# @GitHub : https://github.com/ActStrady/selenium-learn

"""
selenium 的常用操作
"""

from selenium import webdriver

# 获取驱动
from selenium.webdriver.common.keys import Keys

# chrome无界面
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# 获取驱动
driver = webdriver.Chrome(options=options)
# 执行请求 boss直聘
driver.get('https://www.zhipin.com/')
# 获取页面所有信息
HTML = driver.page_source
# 获取input输入框
input_ = driver.find_element_by_class_name('ipt-search')
# 清空
input_.clear()
# 输入信息
input_.send_keys('java')
# 回车
input_.send_keys(Keys.ENTER)
# java招聘信息
java_html = driver.page_source
print(java_html)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
