# -*- coding: utf-8 -*-
import os
import re
import time
from time import sleep

import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
        """

        :param set_name: 指定上传的数据集
        :param data_type: 指定上传的数据类型
        :param file_name: 上传数据文件名
        :return:
        """
        with allure.step("流程代码路径：%s" % __file__):
            pass
        with allure.step('点击数据模块'):
            self.locator(*other_page.page_main_Data_btn).click()
        with allure.step('点击ui-test文件目录'):
            self.locator_explicitly_until(*data_page.page_data_dir_uitest_btn).click()
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
            self.monitor_progress_bar(data_type)
        with allure.step('任务列表状态监测'):
            # 调用数监测任务状态方法
            ele = self.monitor_upload_task_text()
            return ele

    # 监测数据上传进度条
    def monitor_progress_bar(self, data_type, upload_max_time=120):
        """

        :param data_type: 数据类型
        :param upload_max_time: 默认最大上传超时时间120s
        :return:
        """
        if data_type in ['倾斜摄影模型', '影像或栅格文件']:
            upload_max_time = 300
        try:
            # 查找文件上传的进度条为100%,最大超时时间120s
            self.locator_explicitly_until(*data_page.page_progress_bar_text, time=upload_max_time)
            print('文件上传成功')

        except TimeoutException:
            el = self.locator_explicitly_until('xpath', '//div[@class="el-progress__text"]').text
            print(f'文件上传失败，进度为：{el}')
            raise Exception('文件上传超时')

    # 监测数据导入弹窗状态
    def monitor_upload_state(self, import_max_time=180):
        """

        :param import_max_time:数据导入超时时间默认180s
        :return:数据导入结果
        """
        start_time = time.time()
        self.locator_explicitly_until('css selector', '[class="init-store-status-text"]')
        while time.time() - start_time < import_max_time:
            try:
                ele = self.locator_explicitly_until('css selector', '[class="init-store-status-text"]', time=2)
                if ele.text == '正在导入数据':
                    pass
                else:
                    print('数据导入失败')
                    return ele.text

            except TimeoutException:
                self.locator_explicitly_not_until('css selector', '[class="init-store-status-text"]', time=1,
                                                  poll_frequency=0.1)
                return '数据导入成功'

        return '数据导入超时'

    # 监测任务列表中的状态
    def monitor_upload_task_text(self, import_max_time=180):
        self.locator_explicitly_until(*data_page.page_progress_import_statue)
        self.locator_explicitly_until(*data_page.page_progress_close_btn).click()

        start_time = time.time()
        while time.time() - start_time < import_max_time:
            self.locator(*data_page.page_task_btn).click()
            sleep(1)
            task_status = self.locator(*data_page.page_task_first_status).text
            if task_status == '正在导入':
                sleep(5)
                self.locator(*data_page.page_tool_refresh).click()
                continue
            elif task_status in ['导入失败', '导入成功']:
                return task_status

        else:
            return '导入超时'

    # 检查数据概览页面的信息
    def check_data_info(self,set_name, object_name):
        self.locator(*other_page.page_main_Data_btn).click()
        self.get_first_object(set_name, object_name)
        start_time = time.time()
        while time.time() - start_time < 10:
            geography_info = self.locator(*data_page.data_overview_geography).text
            if geography_info in ' 暂无位置信息 ':
                sleep(1)
            else:
                return geography_info


    # 进入指定数据集的指定数据对象概览页面
    def get_first_object(self,set_name, object_name):
        """
        :param set_name: 数据集名称
        :param object_name: 数据对象名称
        :return:
        """

        self.locator_explicitly_until(*data_page.page_data_dir_uitest_btn).click()
        self.locator_explicitly_until('xpath',
                                      '//span[text()="{}" and @class="dataset-span"]'.format(set_name)).click()
        sleep(1)
        # replace=object_name.rstrip(".zip")
        # ele = self.locators('xpath',f'//*[@class="flex-start data-set-body"]//span[contains(text(),"{replace}")]')
        # print(ele)
        # ele[0].click()
        self.locator_explicitly_until('xpath',
                                      '(//*[contains(text(),"{}")]//ancestor::div[@class="set-content-card"])[1]'.format(object_name)).click()

    # 修改数据概览页面中的数据简介
    def change_data_intro(self,set_name, object_name,info):
        """
        :param set_name: 数据集名称
        :param object_name: 数据对象名称
        :param info: 数据简介参数
        :return:
        """
        self.locator(*other_page.page_main_Data_btn).click()

        self.get_first_object(set_name, object_name)
        try:
            self.locator(*data_page.data_overview_intro_btn).click()
        except NoSuchElementException:
            self.locator(*data_page.data_overview_intro_btn2).click()
        self.locator(*data_page.data_overview_intro_input).send_keys(info)
        self.locator(*data_page.data_overview_intro).click()
        text = self.locator(*data_page.data_overview_intro_mes).text
        return text

    # 修改元数据信息
    def change_metadata_info(self,set_name, object_name,mes):
        self.locator(*other_page.page_main_Data_btn).click()
        self.get_first_object(set_name, object_name)
        self.locator(*data_page.data_overview_metadata_btn).click()
        sleep(1)
        self.locator(*data_page.data_overview_metadata_all).click()
        sleep(1)
        self.locator(*data_page.data_overview_metadata_edit).click()
        sleep(2)
        self.locator_explicitly_until(*data_page.data_overview_metadata_input).send_keys(str(mes))
        self.locator(*data_page.data_overview_metadata_submit).click()
        self.locator(*data_page.data_overview_metadata_confirm).click()
        el = self.locator_explicitly_until(*data_page.data_overview_metadata_mes)
        text = el.get_attribute('textContent')
        print(text)
        return text

    def check_data_content(self,set_name, object_name):
        self.locator(*other_page.page_main_Data_btn).click()
        if set_name in ['矢量','正射']:
            self.get_first_object(set_name, object_name)
        else:
            return '跳过'
        self.locator(*data_page.data_overview_content_btn).click()
        if set_name == '矢量':
            self.locator(*data_page.data_overview_content_header)
            sleep(1)
            content_sum = self.locator(*data_page.data_overview_content_sum).text
            content_sum_new = int(''.join(re.findall(r'\d+', content_sum)))
            if content_sum_new != 0:
                return '通过'
            else:
                return '失败'
        elif set_name == '正射':
            try:
                self.locator_explicitly_until(*data_page.data_overview_waveband_name,3)
                return '通过'
            except Exception:
                return '失败'

