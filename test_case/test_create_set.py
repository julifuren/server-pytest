# -*- coding: utf-8 -*-
import allure
import pytest

from kew_word.kewword import pase_yaml
from logic import data_business


@allure.feature('创建数据集测试用例')
@pytest.mark.parametrize('test_data', pase_yaml('data', 'create_set.yaml'))
def test_create_set(browser, login,refresh_driver, test_data):
    allure.dynamic.title(test_data['case'])
    create_set_business = data_business.DataBusiness(browser)
    create_set_business.create_data_set_business(test_data['data_set'])
    result = create_set_business.get_create_result_text()
    assert result == '新建数据集成功'


if __name__ == '__main__':
    pytest.main(['-sv','test_create_set.py'])
