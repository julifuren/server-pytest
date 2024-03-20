import os


import pytest


def run():
    pytest.main(['-v', '--alluredir',
                 './report/result',
                 '--clean-alluredir',
                 # '-k','test_upload_vector',  # -k用于模糊查找指定的用例名
                 './test_case/test_upload_data.py'
                 # '--allure-no-capture'
                 ])
    os.system('allure generate ./report/result/ -o ./report/report_allure/ --clean')


if __name__ == '__main__':
    run()
