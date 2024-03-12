# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from kew_word.kewword import WebKeys
from pages import other_page, data_page

# os.popen("D:\PythonTest\Pie_Server2.0\debug\chrome.bat")
# sleep(3)


options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:9222'
driver = webdriver.Chrome(options=options)
sleep(2)
wk = WebKeys(driver)
# driver.get('https://engine.piesat.cn/server/data/')


# wk.locator(*other_page.page_main_Data_btn).click()  # 点击导航栏数据按钮

# try:
#     wk.locator_explicitly_until(*data_page.page_data_dir_uitest, 3)  # 查找名为ui-test的文件目录

# wk.locator_explicitly_until('xpath','//span[text()="{}" and @class="dataset-span"]'.format('矢量')).click()
# wk.locator(*data_page.page_tool_add_data).click()
# wk.locator(*data_page.page_upload_local_btn).click()
# wk.locator(*data_page.page_data_type_select).click()
# wk.locator_explicitly_until('xpath','//strong[text()="{}"]'.format('矢量数据文件')).click()
# sleep(1)
# wk.locator(*data_page.page_upload_input).send_keys(r'D:\PythonTest\Pie_Server2.0\files\矢量数据文件\道路1706_前_2000.zip')
# wk.locator(*data_page.page_upload_file_status)
# wk.locator_explicitly_until(*data_page.page_upload_file_status,time=60)
el = wk.locator('css selector','[placeholder="请输入验证码"]~img')
print(el.get_attribute('src'))