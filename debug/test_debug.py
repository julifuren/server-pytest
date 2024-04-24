# -*- coding: utf-8 -*-
import os
import re
import urllib.request
from time import sleep

import requests
import urllib3
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from kew_word.kewword import WebKeys, pase_yaml
from logic.data_business import DataBusiness
from pages import other_page, data_page

# os.popen("D:\PythonTest\Pie_Server2.0\debug\chrome.bat")
# sleep(3)


options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:9222'
driver = webdriver.Chrome(options=options)
sleep(2)
wk = WebKeys(driver)
# driver.get('https://engine.piesat.cn/server/data/')


sleep(2)
wk = WebKeys(driver)
a = wk.locators('xpath','//*[@class="flex-start data-set-body"]//span[contains(text(),"region-GK")]')[1]
print(a)
a.click()

