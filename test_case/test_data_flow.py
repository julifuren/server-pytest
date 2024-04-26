# -*- coding: utf-8 -*-
"""
数据流程测试用例
主要测试流程：
1.矢量数据上传-查看概览页面数据信息-修改摘要信息-发布服务-查看元数据信息-编辑元数据信息-查看数据内容-修改数据内容-查看可视化-更改样式保存--查看服务瓦片响应
2.正射数据上传-查看概览页面数据信息-查看元数据信息-编辑元数据信息-查看数据内容-修改数据内容-查看可视化-更改样式保存-发布服务-查看服务瓦片响应
3.正射
"""
import allure
import pytest

from kew_word.kewword import pase_yaml
from logic.data_business import DataBusiness


class TestVectorDataFlow:
    data = pase_yaml('data', 'data_flow.yaml')['case01']

    # 需要执行的用例列表id
    @pytest.mark.skip('跳过')
    @allure.title('上传数据')
    @pytest.mark.dependency()  # 代表这条用例为主条件
    # @pytest.mark.xfail(reason="deliberate fail")  #标记用例直接为失败
    def test_upload_data(self, browser, login):
        data = self.data['data_info']
        data_business = DataBusiness(browser)
        result = data_business.upload_data_business(data['data_set'], data['data_type'], data['file_name'])
        assert result == '导入成功'

    # @pytest.mark.skip('跳过')
    # @pytest.mark.dependency(depends=["test_upload_data"])  # 设置用例依赖，依赖 test_upload_data
    @allure.title('检查数据地理位置信息')
    def test_check_geography_info(self, browser, login):
        data = self.data['data_info']
        check_business = DataBusiness(browser)
        result = check_business.check_data_info(data['data_set'], data['object_name'])
        assert result in data['overview']['geographic_location']

    # @pytest.mark.skip('跳过')
    @allure.title('修改数据简介内容')
    def test_change_data_intro(self, browser, login):
        data = self.data['data_info']
        change_business = DataBusiness(browser)
        result = change_business.change_data_intro(data['data_set'], data['object_name'],
                                                   data['overview']['data_intro'])
        assert result == '更新摘要成功！'

    # @pytest.mark.skip('跳过')
    @allure.title('修改元数据信息')
    def test_change_metadata_info(self, browser, login):
        data = self.data['data_info']
        metadata_business = DataBusiness(browser)
        result = metadata_business.change_metadata_info(data['data_set'], data['object_name'],
                                                        data['overview']['metadata'])
        assert result == '提交成功!'

    # @pytest.mark.skip('跳过')
    @allure.title('检查数据内容页面')
    def test_check_data_content(self, browser, login):
        data = self.data['data_info']
        content_business = DataBusiness(browser)
        result = content_business.check_data_content(data['data_set'], data['object_name'])
        assert result == '通过'

    @allure.title("可视化样式配置")
    def test_change_data_style(self, browser, login):
        image_business = DataBusiness(browser)
        data = self.data['data_info']
        result = image_business.change_data_style(data['data_set'], data['object_name'])
        assert result == '保存成功'

    @allure.title('发布服务')
    def test_release_server(self, browser, login):
        release_business = DataBusiness(browser)
        data = self.data['data_info']
        result = release_business.release_serve(data['data_set'], data['object_name'])
        assert result == '发布成功'

    def test_server_preview(self):
        pass



if __name__ == '__main__':
    # pytest.main(['-vs', 'test_data_flow.py::TestVectorDataFlow::test_upload_data'])
    pytest.main(['-vs', 'test_data_flow.py::TestVectorDataFlow::test_release_server',
                 '-pno:warnings'

                 ])
