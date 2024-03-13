# -*- coding: utf-8 -*-
"""
数据页面元素
"""
# 添加目录按钮
page_create_dir_btn = ('xpath', '//span[@title="添加目录"]')
# 目录名称输入框
page_dir_name_input = ('css selector', '[placeholder="请输入目录名称"]')
# 数据目录为ui-test 的文件目录
page_data_dir_uitest = ('xpath', '//span[text()="ui-test"]')
# 数据目录为ui-test 的文件目录展开按钮
page_data_dir_uitest_btn = ('xpath', '//span[text()="ui-test"]/../../preceding-sibling::span')
# 创建数据集+按钮
page_create_set_btn = ('css selector', '[class="edit-image"] [class="el-image__inner"]')
# 工具栏添加数据按钮
page_tool_add_data = ('css selector', '[class="btn-item"]:nth-child(2) [class="el-image el-tooltip"]')

"""
创建数据集弹窗元素
"""
# 创建数据集弹窗-标题输入框
page_create_set_pop_title = ('css selector', '[placeholder="数据集名称"]')
# 创建数据集弹窗-创建按钮
page_create_set_pop_create_btn = ('xpath', '//span[text()="创 建"]')
# 创建数据集后的提示弹窗
page_create_set_prompt_info = ('css selector', '[class="el-message__content"]')

"""
添加数据弹窗元素
"""
# 添加数据弹窗通过本地文件上传
page_upload_local_btn = ('xpath', '//strong[text()="通过本地文件上传数据"]')
# 数据类型选择下拉框
page_data_type_select = ('xpath', '//div[@class="upload-container"]/div/div[@class="flex-start"]')
# 文件上传input框
page_upload_input = ('xpath', "//input[@name='file']")
# 文件上传成功后标识
page_upload_file_status = ('css selector', '[class="el-icon-document"]')
# 添加数据弹窗中的 导入或解析 按钮
page_upload_import_btn = ('css selector','[class="add-data-footer flex-end"]>span div span')
# csv文件的二次导入按钮
page_upload_csv_import_btn = ('xpath', '//span[text()="导 入"]')
# 添加数据弹窗中的 进度条100%
page_progress_bar_text = ('xpath', '//div[text()="100%"]')
