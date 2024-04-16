# -*- coding: utf-8 -*-
"""
数据流程测试用例
主要测试流程：
1.矢量数据上传-查看概览页面数据信息-修改摘要信息-发布服务-查看元数据信息-编辑元数据信息-查看数据内容-修改数据内容-查看可视化-更改样式保存--查看服务瓦片响应
2.正射数据上传-查看概览页面数据信息-查看元数据信息-编辑元数据信息-查看数据内容-修改数据内容-查看可视化-更改样式保存-发布服务-查看服务瓦片响应
3.正射
"""
import pytest

from logic.login_business import LoginBusiness


class TestDataFlow:

    # @classmethod
    # def setup_class(cls):
    #     pass
    #
    # @classmethod
    # def teardown_class(cls):
    #     print("teardown_class======================")

    def test_demo(self):
        print('111')


if __name__ == '__main__':
    pytest.main(['-s', 'test_data_flow.py'])
