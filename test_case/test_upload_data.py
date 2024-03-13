# -*- coding: utf-8 -*-
import allure
import pytest

from kew_word.kewword import pase_yaml
from logic.data_business import DataBusiness


class TestUploadData:

    # 解析数据上传测试用例数据
    data = pase_yaml('data','upload_data.yaml')

    # @pytest.mark.skip
    @allure.title(data['case01']['case_name'])
    def test_upload_vector(self,browser, login,refresh_driver):
        case = self.data['case01']
        upload_data = DataBusiness(browser)
        upload_data.upload_data_business(case['data_set'], case['data_type'], case['file_name'])

    @pytest.mark.skip
    @allure.title(data['case02']['case_name'])
    def test_upload_dom(self, browser, refresh_driver):
        case = self.data['case02']
        upload_data = DataBusiness(browser)
        upload_data.upload_data_business(case['data_set'], case['data_type'], case['file_name'])

    @allure.title(data['case05']['case_name'])
    def test_upload_csv(self, browser, refresh_driver):
        case = self.data['case05']
        upload_data = DataBusiness(browser)
        upload_data.upload_data_business(case['data_set'], case['data_type'], case['file_name'])