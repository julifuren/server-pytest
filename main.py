import os

import pytest


def run():
    pytest.main(['-v',
                 '--alluredir', './report/result', '--clean-alluredir',
                 # '-n', '3',   # 设置多进程  auto:自动
                 # '-k','test_upload_vector',  # -k用于模糊查找指定的用例名
                 './test_case/test_data_flow.py',  # 运行指定的测试文件
                 # '--allure-no-capture'  # 取消日志或者print输出到allure测试报告中
                 '-pno:warnings'  # 完全禁用警告捕获
                 ])
    os.system('allure generate ./report/result/ -o ./report/report_allure/ --clean')


if __name__ == '__main__':
    run()
