# -*- coding: utf-8 -*-

import allure
import pytest
from selenium import webdriver

from logic.login_business import LoginBusiness


@allure.title('刷新浏览器')
@pytest.fixture(scope='function', autouse=True)
def refresh_driver(browser):
    driver = browser
    driver.refresh()


# 登录业务fixture
@allure.title('执行登录操作')
@pytest.fixture(scope='module')
def login(browser):
    login_business = LoginBusiness(browser)
    login_business.open_url()  # 打开config.yaml文件中对应的url
    login_business.login('account01')  # login_data.yaml中的登录的账号


@allure.title('初始化driver')
@pytest.fixture(scope='module')
def browser():
    """
    全局定义浏览器驱动，方便下面的hook函数引用driver
    :return:
    """
    global driver

    with allure.step('打开浏览器'):
        # 加载浏览器驱动
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')  # 最大化(无头模式下无法使用)

        options.add_argument('--headless')  # 无头模式下运行
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

        # options = webdriver.Edge()
        #
        # options.add_argument('start-maximized')
        # driver = webdriver.Chrome(options=options)

    # 隐式等待5秒
    driver.implicitly_wait(5)

    """
    yield之前的代码是用例前置
    yield之后的代码是用例后置
    """
    yield driver
    # 浏览器退出
    with allure.step('退出浏览器'):
        driver.quit()
        """
            这种debug模式，下面的方法无法退出浏览器
            driver.quit()
            driver.close()
        """
        # 通过命令杀死进程
        # os.system('taskkill /im chromedriver.exe /F')
        # os.system('taskkill /im chrome.exe /F')


# 用例失败截图fixture
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 可以获取测试用例的执行结果，yield，返回一个result对象
    out = yield
    """
        从返回一个result对象（out）获取调用结果的测试报告，返回一个report对象
        report对象的属性
        包括when(setup,call,teardown三个值)、nodeid(测试用例的名字)、
        outcome(用例的执行结果：passed,failed)
    """
    report = out.get_result()
    # 仅仅获取用例call阶段的执行结果，不包含setup和teardown
    if report.when == 'call':
        # 获取用例call执行结果为结果为失败的情况
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("====================用例失败截图===================="):
                # 使用allure自带的添加附件的方法：三个参数分别为：源文件、文件名、文件类型
                allure.attach(driver.get_screenshot_as_png(), "失败截图",
                              allure.attachment_type.PNG)
