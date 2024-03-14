# -*- coding: utf-8 -*-
import os
import time
from time import sleep

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from kew_word.kewword import WebKeys, get_project_path
from pages import other_page, data_page


class DataBusiness(WebKeys):

    # 创建数据集流程
    def create_data_set_business(self, data_set_name):
        with allure.step("流程代码路径：%s" % __file__):
            pass
        dir_exist = True
        # with allure.step('刷新浏览器'):
        #     self.driver.refresh()
        with allure.step('点击导航栏数据按钮'):
            self.locator(*other_page.page_main_Data_btn).click()  # 点击导航栏数据按钮

        with allure.step('查找ui-test文件目录'):
            try:
                self.locator_explicitly_until(*data_page.page_data_dir_uitest, 3)  # 查找名为ui-test的文件目录

            except TimeoutException:
                print('ui-test目录不存在')
                dir_exist = False

        if not dir_exist:
            # 一级目录不存在进行创建一级目录
            with allure.step('ui-test目录不存在，开始创建'):
                self.locator(*data_page.page_create_dir_btn).click()
                self.locator(*data_page.page_dir_name_input).send_keys('ui-test')
                self.locator(*data_page.page_dir_name_input).send_keys(Keys.ENTER)

        with allure.step('创建数据集'):
            # 点击ui-test目录的'创建数据集'按钮
            ele = self.locator(*data_page.page_data_dir_uitest)
            ActionChains(self.driver).move_to_element(ele).perform()
            sleep(1)
            self.locator(*data_page.page_create_set_btn).click()

            # 输入数据集名称
            self.locator(*data_page.page_create_set_pop_title).send_keys(data_set_name)

            # 点击创建按钮
            self.locator(*data_page.page_create_set_pop_create_btn).click()

    # 获取创建数据集后的提示语
    def get_create_result_text(self):

        el = self.locator_explicitly_until(*data_page.page_create_set_prompt_info)
        text = el.get_attribute('textContent')
        sleep(1)
        return text

    # 上传数据业务流程
    def upload_data_business(self, set_name, data_type, file_name):
        with allure.step("流程代码路径：%s" % __file__):
            pass
        with allure.step('点击数据模块'):
            self.locator(*other_page.page_main_Data_btn).click()
        with allure.step('点击ui-test文件目录'):
            self.locator(*data_page.page_data_dir_uitest_btn).click()
        with allure.step(f'点击{set_name}数据集'):
            self.locator_explicitly_until('xpath',
                                          '//span[text()="{}" and @class="dataset-span"]'.format(set_name)).click()
        with allure.step('点击添加数据按钮'):
            self.locator(*data_page.page_tool_add_data).click()
        with allure.step('选择通过本地上传‘'):
            self.locator(*data_page.page_upload_local_btn).click()
        with allure.step(f'选择上传的数据类型为{data_type}'):
            # 点击数据类型下拉框
            self.locator(*data_page.page_data_type_select).click()
            # 选择数据类型
            self.locator_explicitly_until('xpath', '//strong[text()="{}"]'.format(data_type)).click()
            sleep(1)
        with allure.step('上传文件'):
            # 上传文件
            data_path = os.path.join(get_project_path(), 'files', data_type, file_name)
            # 输入文件路径
            self.locator(*data_page.page_upload_input).send_keys(data_path)
            # 定位文件上传成功后的标识
            self.locator_explicitly_until(*data_page.page_upload_file_status, time=60)
        with allure.step('上传文件进度百分比监测'):
            # 点击导入或解析按钮
            self.locator(*data_page.page_upload_import_btn).click()
            if data_type == '带有坐标信息的表格文件':
                self.locator(*data_page.page_upload_csv_import_btn).click()
            else:
                pass
            # 调用监测数据上传进度条方法
            self.monitor_progress_bar()
        with allure.step('导入文件状态监测'):
            # 调用监测弹窗状态方法
            self.monitor_upload_state()

    # 监测数据上传进度条
    def monitor_progress_bar(self, upload_max_time=300):
        """

        :param upload_max_time: 默认最大上传超时时间300s
        :return:
        """
        try:
            # 查找文件上传的进度条为100%,最大超时时间300s
            self.locator_explicitly_until(*data_page.page_progress_bar_text, time=upload_max_time)
            print('文件上传成功')

        except TimeoutException:
            el = self.locator_explicitly_until('xpath', '//div[@class="el-progress__text"]').text
            print(f'文件上传失败，进度为：{el}')
            raise Exception('文件上传超时')

    # 监测数据导入弹窗状态
    def monitor_upload_state(self, import_max_time=180):
        '''

        :param import_max_time:数据导入超时时间默认180s
        :return:数据导入结果
        '''
        self.locator_explicitly_until('css selector', '[class="init-store-status-text"]')
        start_time = time.time()
        while time.time() - start_time < import_max_time:
            try:
                self.locator_explicitly_not_until('css selector', '[class="init-store-status-text"]', time=1,poll_frequency=0.1)
                print('导入成功')
                return '数据导入成功'

            except TimeoutException:

                ele = self.locator_explicitly_until('css selector', '[class="init-store-status-text"]')
                if ele.text == '正在导入数据':
                    pass
                else:
                    print('数据导入失败')
                    return ele.text
