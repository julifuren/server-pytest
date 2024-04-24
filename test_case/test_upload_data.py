# -*- coding: utf-8 -*-
import allure
import pytest

from kew_word.kewword import pase_yaml
from logic.data_business import DataBusiness


class TestUploadData:
    # 解析数据上传测试用例数据
    data = pase_yaml('data', 'upload_data.yaml')
    vector = data['vector']
    dom = data['dom']
    jsons = data['json']
    gdb = data['GDB']
    coordinate = data['coordinate']
    document = data['document']
    media = data['media']
    dem = data['DEM']
    osgb = data['OSGB']


    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', vector)
    def test_upload_vector(self, browser, all_data, login):
        # allure.dynamic.story('矢量类型数据上传')
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', dom)
    def test_upload_dom(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', jsons)
    def test_upload_json(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', gdb)
    def test_upload_gdb(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', coordinate)
    def test_upload_coordinate(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', document)
    def test_upload_document(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', media)
    def test_upload_media(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', dem)
    def test_upload_dem(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'

    @allure.feature('数据上传测试用例')
    @pytest.mark.parametrize('all_data', osgb)
    def test_upload_osgb(self, browser, all_data):
        allure.dynamic.title(all_data['case_name'])
        upload_data = DataBusiness(browser)
        result = upload_data.upload_data_business(all_data['data_set'], all_data['data_type'], all_data['file_name'])
        assert result == '导入成功'
