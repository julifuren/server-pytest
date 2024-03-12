# -*- coding: utf-8 -*-
import allure
import pytest

from kew_word.kewword import pase_yaml
from logic.data_business import DataBusiness


class TestUploadData:

    # 解析数据上传测试用例数据
    data = pase_yaml('data','upload_data.yaml')

    @allure.title('矢量面数据上传')
    # 上传矢量面数据
    def test_upload_vector(self,browser, login,refresh_driver):
        case = self.data['case01']
        upload_data = DataBusiness(browser)
        upload_data.upload_data_business(case['data_set'], case['data_type'], case['file_name'])

    @allure.title('正射数据上传')
    # 上传正射数据
    def test_upload_dom(self, browser, refresh_driver):
        case = self.data['case02']
        upload_data = DataBusiness(browser)
        upload_data.upload_data_business(case['data_set'], case['data_type'], case['file_name'])



# @pytest.mark.parametrize('test_data', pase_yaml('data', 'upload_data.yaml'))
# def test_upload_data(browser, login,refresh_driver, test_data):
#     upload_data = DataBusiness(browser)
#     upload_data.upload_data_business(test_data['data_set'], test_data['data_type'], test_data['file_name'])
