# -*- coding: utf-8 -*-
import urllib.request
from time import sleep
import time
from selenium.common.exceptions import TimeoutException

from other.pase_verificationcode import *
from pages import other_page


class LoginBusiness(WebKeys):

    def input_userinfo(self, username, pwd):
        self.locator(*other_page.page_login_User).send_keys(username)
        self.locator(*other_page.page_login_Pwd).send_keys(pwd)

    @allure.step("开始登陆")
    def login(self, account_num):
        """

        :param url: 登录url
        :param account_num: 需要登录的账户序号
        :return:
        """
        with allure.step("流程代码路径：%s" % __file__):
            pass
        # 解析配置文件
        pase_data = pase_yaml('config', 'config.yaml')
        # 解析登录账号数据
        data = pase_yaml('config', 'login_data.yaml')

        if pase_data['yzm']:
            print('开启验证码登录')
            # 限制最大登录次数
            max_attempts = 10
            attempts = 1
            while attempts <= max_attempts:
                if attempts == 5:
                    print(f'登录失败次数已达到{attempts}次，等待5分钟后再次尝试登录')
                    sleep(300)

                with allure.step(f'输入账号:{data[account_num]["username"]} 输入密码：{data[account_num]["pwd"]}'):
                    # 输入账号和密码
                    self.input_userinfo(data[account_num]['username'], data[account_num]['pwd'])

                with allure.step('图像识别解析验证码'):
                    yanzheng = self.pase_yam()
                    self.locator(*other_page.page_login_verificationcode).send_keys(yanzheng)
                with allure.step(f'尝试第{attempts}次登录'):
                    self.locator(*other_page.page_login_btn).click()
                    sleep(1)
                    try:
                        # self.driver.implicitly_wait(1)
                        self.locator_explicitly_until(*other_page.page_verificationcode_text, time=1)
                        self.driver.refresh()
                        attempts += 1
                        continue

                    except TimeoutException:
                        self.driver.implicitly_wait(2)
                        self.locator_explicitly_until(*other_page.page_main_Data_btn, time=2)
                        print('检测到导航栏 数据 模块，登录成功')
                        self.driver.implicitly_wait(5)
                        break

                    # finally:
                    #     # 重置隐士等待时间
                    #     self.driver.implicitly_wait(5)
            else:
                raise Exception("登录失败，已尝试登录{}次".format(max_attempts))

        elif not pase_data['yzm']:
            with allure.step(f'输入账号:{data[account_num]["username"]} 输入密码：{data[account_num]["pwd"]}'):
                self.input_userinfo(data[account_num]['username'], data[account_num]['pwd'])
                self.locator(*other_page.page_login_btn).click()
            try:
                self.locator_explicitly_until(*other_page.page_main_Data_btn, time=3)
                print('检测到导航栏 数据 模块，登录成功')

            except TimeoutException:
                raise Exception('未检测到导航栏中的 数据 按钮，请检查是否登录成功')

    def pase_yam(self):
        sleep(1)
        el = self.locator(*other_page.page_verificationcode_pic)
        url = el.get_attribute('src')
        file_path = os.path.join(get_project_path(), 'other')
        # timestamp = int(time.time())

        # time_stamp = f"file_{os.getpid()}_{timestamp}.png"
        # file_name = file_path + "\\" + time_stamp
        file_name = file_path + "\\" + 'yzm.png'


        urllib.request.urlretrieve(url, file_name)
        yzm = parse_yanzheng(file_name)
        return yzm


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    test = LoginBusiness(driver)
    test.open_url('url-formal')
    test.login('account02', 'url-formal')
