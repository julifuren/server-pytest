# -*- coding: utf-8 -*-
from time import sleep

import allure
import requests

from kew_word.kewword import WebKeys
from pages import other_page, server_page


class ServerBusiness(WebKeys):

    # 服务预览
    def server_preview(self, server_name, x, y, z):
        self.locator(*other_page.page_main_Server_btn).click()
        # 点击我的按钮
        self.locator(*server_page.ser_toolbar_my_btn).click()
        # 找到第一个名为server_name的服务
        self.locator_explicitly_until('xpath',
                                      f'(//p[contains(text(),"{server_name}") and '
                                      '@class="data-card-title"]//ancestor::div[@class="data-card"])[1]').click()

        self.locator(*server_page.ser_overview_layer_unfold).click()
        sleep(1)

        # 获取服务地址并处理
        el = self.locator(*server_page.ser_overview_server_value)
        js = 'arguments[0].scrollIntoView()'
        self.driver.execute_script(js, el)
        url = el.get_attribute('value')
        new_url = url.format(x=x, y=y, z=z)
        with allure.step(f'获取服务地址为：{new_url}'):
            pass
        with allure.step('服务瓦片预览'):
            # 获取接口响应的大小：content_length
            res = requests.get(new_url)
        return res.status_code

    # 删除服务
    def delete_server(self, server_name):
        self.locator(*other_page.page_main_Server_btn).click()
        self.locator(*server_page.ser_toolbar_my_btn).click()
        self.locator(*server_page.ser_toolbar_all_ser).click()

        # 点击第一个名为server_name服务的勾选按钮
        self.locator_explicitly_until('xpath', f'(//p[contains(text(),"{server_name}") and @class="data-card-title'
                                               f'"]//ancestor::div[@class="data-card"])[1]//span['
                                               f'@class="el-checkbox__inner"]').click()
        sleep(1)
        self.locator(*server_page.ser_toolbar_delete_btn).click()
        self.locator(*server_page.ser_pop_delete_btn).click()
        el = self.locator(*server_page.ser_delete_mes)
        text = el.get_attribute('textContent')
        return text
