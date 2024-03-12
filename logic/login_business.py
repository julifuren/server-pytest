# -*- coding: utf-8 -*-
import urllib.request
from time import sleep

from other.pase_verificationcode import *
from pages import other_page


class LoginBusiness(WebKeys):

    def input_userinfo(self, username, pwd):
        self.locator(*other_page.page_login_User).send_keys(username)
        self.locator(*other_page.page_login_Pwd).send_keys(pwd)

    @allure.step("开始登陆")
    def login(self, account_num, url):
        """

        :param url: 登录url
        :param account_num: 需要登录的账户序号
        :return:
        """
        with allure.step("流程代码路径：%s" % __file__):
            pass
        # 解析配置文件
        pase_data = pase_yaml( 'config', 'config.yaml')
        # 解析登录账号数据
        data = pase_yaml('config', 'login_data.yaml')

        if pase_data['yzm']:
            print('开启验证码登录')
            # 限制最大登录次数
            max_attempts = 5
            attempts = 1
            while attempts <= max_attempts:
                with allure.step(f'输入账号:{data[account_num]["username"]} 输入密码：{data[account_num]["pwd"]}'):
                    # 输入账号和密码
                    self.input_userinfo(data[account_num]['username'], data[account_num]['pwd'])
                with allure.step('图像识别解析验证码'):
                    # 解析输入验证码
                    yanzheng = parse_yanzheng(url)
                    self.locator(*other_page.page_login_verificationcode).send_keys(yanzheng)
                with allure.step(f'尝试第{attempts}次登录'):
                    self.locator(*other_page.page_login_btn).click()
                    try:
                        fail_login_text = self.locator_explicitly_until(*other_page.page_login_fail_pop_ele, 2,
                                                                        poll_frequency=0.5).text
                        # fail_login_text = el.get_attribute('textContent')
                        print(fail_login_text)
                        if fail_login_text in ' 此帐号操作失败多次已被锁定5分钟 ':
                            print('开始等待5分钟')
                            sleep(300)
                            self.driver.refresh()
                            attempts += 1
                        elif fail_login_text in '图形验证码输入有误':
                            self.driver.refresh()
                            attempts += 1

                        else:
                            self.driver.refresh()
                            attempts += 1

                    except:
                        # 重新设置隐士等待时间为1s
                        # self.driver.implicitly_wait(1)
                        # 查找登录后的导航栏 数据 按钮
                        self.locator_explicitly_until(*other_page.page_main_Data_btn,time=3)
                        print('登录成功')
                        break

                if attempts == max_attempts:
                    raise Exception("登录失败，已尝试登录{}次".format(max_attempts))

    # @allure.step("开始登陆")
    # def login(self, account_num):
    #     """
    #
    #     :param url: 登录url
    #     :param account_num: 需要登录的账户序号
    #     :return:
    #     """
    #
    #     # 解析配置文件
    #     pase_data = pase_yaml('config', 'config.yaml')
    #     # 解析登录账号数据
    #     data = pase_yaml('config', 'login_data.yaml')
    #
    #     if pase_data['yzm']:
    #         print('开启验证码登录')
    #         # 限制最大登录次数
    #         max_attempts = 5
    #         attempts = 1
    #         while attempts <= max_attempts:
    #             # 输入账号和密码
    #             self.input_userinfo(data[account_num]['username'], data[account_num]['pwd'])
    #             # 定位到验证码图像
    #             code = self.locator(*other_page.page_verificationcode_pic)
    #             # 获取验证码元素中的src属性值拿到图片下载地址
    #             code_down_link = code.get_attribute('src')
    #             # 设置图片保存路径
    #             path = os.path.join(get_project_path(), 'other', 'yzm.jpg')
    #             # 下载图片
    #             urllib.request.urlretrieve(code_down_link, path)
    #
    #             # 解析输入验证码
    #             yanzheng = parse_yanzheng(path)
    #             self.locator(*other_page.page_login_verificationcode).send_keys(yanzheng)
    #
    #             self.locator(*other_page.page_login_btn).click()
    #             try:
    #                 fail_login_text = self.locator_explicitly_until(*other_page.page_login_fail_pop_ele, 2,
    #                                                                 poll_frequency=0.5).text
    #                 print(fail_login_text)
    #                 if fail_login_text in ' 此帐号操作失败多次已被锁定5分钟 ':
    #                     print('开始等待5分钟')
    #                     sleep(300)
    #                     self.driver.refresh()
    #                     attempts += 1
    #                 elif fail_login_text in '图形验证码输入有误':
    #                     self.driver.refresh()
    #                     attempts += 1
    #                 else:
    #                     self.driver.refresh()
    #                     attempts += 1
    #             except:
    #                 # 查找登录后的导航栏 数据 按钮
    #                 self.locator_explicitly_until(*other_page.page_main_Data_btn, time=3)
    #                 print('登录成功')
    #                 break
    #
    #         if attempts == max_attempts:
    #             raise Exception("登录失败，已尝试登录{}次".format(max_attempts))


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    test = LoginBusiness(driver)
    test.open_url('url-formal')
    test.login('account03')
