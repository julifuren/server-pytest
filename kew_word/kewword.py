# -*- coding: utf-8 -*-

import os

import allure
import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

"""
类外面封装一些共用的方法
"""


# 解析yaml文件数据；
def pase_yaml(path, file_name):
    """

    :param path: 文件夹路径，只能为config或data
    :param file_name: 要读取的yaml文件名
    :return:
    """
    if path in ['config', 'data']:
        file_path = os.path.join(get_project_path(), path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    else:
        raise Exception(f'文件：{path}路径不合法')


# 获取工程路径
def get_project_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""
主要封装selenium的一些常用方法
"""


class WebKeys:
    # 构造方法，接受driver对象
    def __init__(self, driver):
        self.driver = driver

        # 编写代码为了自动关联出代码，写完后注释掉，不然会多开一个浏览器
        # self.driver = webdriver.Chrome()

    @allure.step('打开网址')
    def open_url(self):
        data = pase_yaml('config', 'config.yaml')
        with allure.step(f"打开网址{data['url']}"):
            self.driver.get(data['url'])

        # with allure.step(f'打开网址{url_data}'):
        #     self.driver.get(url_data)

    # 元素定位方法封装
    def locator(self, name, value):
        """

        :param name: 元素定位方式
        :param value: 元素定位的路径
        :return:
        """

        el = self.driver.find_element(name, value)
        self.locator_station(el)
        return el

    # 显示定位的地方，方便确认定位位置
    def locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid green"  # 边框，green绿色
        )

    # 显示等待定位元素
    def locator_explicitly_until(self, name, value, time=10, poll_frequency=0.2):
        ele = WebDriverWait(self.driver, time, poll_frequency).until(ES.presence_of_element_located((name, value)))
        return ele

    # 显示等待定位元素直到元素消失
    def locator_explicitly_not_until(self, name, value, time=10, poll_frequency=0.2):
        # el = WebDriverWait(self.driver, timeout=time, poll_frequency=0.5).until(
        #     lambda el1: self.driver.find_element(name, value), message='显式等待失败')
        el = WebDriverWait(self.driver, time, poll_frequency).until_not(ES.presence_of_element_located((name, value)),
                                                                        message='显示等待失败')
        return el

    def find_element_explicitly(self, locator, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located(locator))


if __name__ == '__main__':
    # path = get_project_path()
    # print(os.path.join(path, 'other'))
    # print(pase_yaml('config', 'login_data.yaml'))
    # data = pase_yaml('data','create_set.yaml')
    # vector = data['vector']
    # print(data)
    data2 = pase_yaml('config', 'config.yaml')
    print(data2['url'])
