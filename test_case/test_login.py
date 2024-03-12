# -*- coding: utf-8 -*-
import allure
import pytest

from logic.login_business import LoginBusiness


@pytest.mark.skip
@allure.title('普通用户登录')
def test_login(browser):
    login_business = LoginBusiness(browser)
    login_business.open_url('url-formal')
    login_business.login('account01','url-formal')
