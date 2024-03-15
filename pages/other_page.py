# -*- coding: utf-8 -*-

"""
导航栏中所有的元素
"""
# 导航栏 数据 按钮
page_main_Data_btn = ('xpath', '//span[@class="item-text" and text()="数据"]')
# 导航栏 服务 按钮
page_main_Server_btn = ('xpath', '//span[@class="item-text" and text()="服务"]')
# 导航栏 场景 按钮
page_main_Scene_btn = ('xpath', '//span[@class="item-text" and text()="场景"]')
# 导航栏 发现 按钮
page_main_Discovery_btn = ('xpath', '//span[@class="item-text" and text()="发现"]')
# 导航栏 集市 按钮
page_main_Market_btn = ('xpath', '//span[@class="item-text" and text()="集市"]')
# 导航栏 应用 按钮
page_main_Application_btn = ('xpath', '//div[@class="nav-list"]//span[text()="应用"]')
# 导航栏 开发 按钮
page_main_Develop_btn = ('xpath', '//div[@class="nav-list"]//span[text()="发开"]')

# 未登录页面 登录 按钮
page_main_login_btn = ('xpath', '//div[text()="登录"]')

"""
登录页面所有元素
"""
# 用户名输入框
page_login_User = ('css selector', '[id="input-1"]')
# 密码输入框
page_login_Pwd = ('css selector', '[id="input-3"]')
# 验证码输入框
page_login_verificationcode = ('css selector', '[id="input-2"]')
# 登录按钮
page_login_btn = ('css selector', '[id="agreement"]')
# 登录失败提示弹窗
page_login_fail_pop_ele = ('xpath', '//div[@class="text-center mb-2"]//span[2]')
# 验证码图片
page_verificationcode_pic = ('css selector','[placeholder="请输入验证码"]~img')
# 验证码登录文本
page_verificationcode_text = ('xpath','//span[text()="验证码登录"]')
