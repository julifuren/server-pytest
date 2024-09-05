import os

import pytest


def run():
    pytest.main(['-v',
                 '--alluredir', './report/result',
                 '--clean-alluredir',  # 清除allure之前生成的json数据
                 # '-n', '3',   # 设置多进程  auto:自动
                 # '-k','test_change_data_style',  # -k用于模糊查找指定的用例名
                 './test_case/test_upload_data.py::TestUploadData::test_upload_vector',  # 运行指定的测试文件
                 # '--allure-no-capture'  # 取消日志或者print输出到allure测试报告中
                 '-pno:warnings'  # 完全禁用警告捕获
                 ])
    # os.system('allure generate ./report/result/ -o ./report/report_allure/ --clean')  #
    # os.system('allure serve ./report/result/ --host 127.0.0.1 --port 9999')


if __name__ == '__main__':
    run()
