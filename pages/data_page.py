# -*- coding: utf-8 -*-
"""
数据一级页面元素
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
# 工具栏：添加数据按钮
page_tool_add_data = ('xpath', '//div[@class="group-info-left flex-start"]//div[2]/*')
# 工具栏：删除数据按钮
page_tool_delete = ('xpath', '//div[@class="group-info-left flex-start"]/div[3]/*')
# 工具栏：添加刷新按钮
page_tool_refresh = ('xpath', '//div[@class="group-info-left flex-start"]/div[6]/*')

# 导航栏的任务按钮
page_task_btn = ('css selector', '[class="i-icon i-icon-transaction-order"]')
# 任务列表中的第一条任务
page_task_first_status = ('xpath', '//*[@class="status-card-content"]/div[1]//div[@class="status-judge"]/span')
# 删除数据弹窗删除按钮
page_pop_delete_btn = ('xpath','//*[@aria-label="删除数据"]//span[text()="删 除"]')
# 删除数据后提示语
page_delete_mes = ('xpath','//p[@class="el-message__content"]')

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
page_upload_import_btn = ('css selector', '[class="add-data-footer flex-end"]>span div span')
# csv文件的二次导入按钮
page_upload_csv_import_btn = ('xpath', '//span[text()="导 入"]')
# 添加数据弹窗中的 进度条100%
page_progress_bar_text = ('xpath', '//div[text()="100%"]')
# 添加数据弹窗 关闭 按钮
page_progress_close_btn = ('xpath', '//div[contains(@class,"create-type")]//i')
# 添加数据弹窗 数据导入 文本
page_progress_import_statue = ('css selector', '[class="init-store-status-text"]')

"""
数据概览页面元素
"""
# 数据概览： '地理位置'
data_overview_geography = ('xpath', '//p[text()="地理位置"]/following-sibling::p')
# 数据概览： 修改数据简介按钮
data_overview_intro_btn = ('xpath', '//div[@class="edit-tool tool-hover"]')
# 数据概览： 修改数据简介按钮2
data_overview_intro_btn2 = ('xpath', '//p[contains(text(),"简要描述")]')
# 数据概览： 数据简介 输入框
data_overview_intro_input = ('css selector', '[class="input-box"] div textarea')
# 数据概览：用于点击使数据简介生效
data_overview_intro = ('xpath', "//p[text()='数据简介']")
# 数据概览：数据简介修改成功后的提示语
data_overview_intro_mes = ('css selector', '[class="el-message__content"]')
# 数据概览：发布-按钮
data_overview_release_btn = ('xpath', "//span[text()='发布数据']")
# 数据概览：发布-服务名称输入框
data_overview_release_input = ('css selector', '[placeholder="服务名称"]')
# 数据概览：发布-服务弹窗下一步
data_overview_release_next = ('xpath', "//span[text()='下一步']")
# 数据概览：发布-服务弹窗 发布按钮
data_overview_release_btn2 = ('xpath', "//span[text()='发 布']")
# 数据概览：发布-发布成功提示语
data_overview_release_mes = ('xpath', '//p[@class="el-message__content"]')


# 元数据按钮
data_overview_metadata_btn = ('xpath', "//div[text()='元数据']")
# 数据内容按钮
data_overview_content_btn = ('xpath', "//div[text()='数据内容']")
# 可视化按钮
data_overview_image_btn = ('xpath', "//div[text()='可视化']")

# 元数据：全部元数据按钮
data_overview_metadata_all = ('xpath', "//div[text()='全部数据项']/..//span")
# 元数据：元数据编辑按钮
data_overview_metadata_edit = ('xpath', "//span[text()=' 编 辑 ']")
# 元数据：元数据提交按钮
data_overview_metadata_submit = ('xpath', "//span[text()='提 交']")
# 元数据：元数据成果代号文本输入框
data_overview_metadata_input = ('xpath', "//label[text()='成果代号']//following-sibling::div//input")
# 元数据：元数据确认弹窗中 确定 按钮
data_overview_metadata_confirm = ('xpath', "//span[text()='确 定']")
# 元数据：元数据修改成功后的提示语
data_overview_metadata_mes = ('xpath', "//p[text()='提交成功!']")
# 元数据：矢量数据的表头
data_overview_content_header = ('css selector', '[class="el-table__header"]')
# 元数据：矢量数据内容总条数
data_overview_content_sum = ('xpath', '//div[@class="el-pagination is-background"]/span[1]')
# 元数据：正射数据内容中的波段名称表头
data_overview_waveband_name = ('xpath', "//div[text()='波段名称']")

# 可视化：样式配置按钮
data_overview_image_config = ('css selector', '[title="样式配置"]')
# 可视化：样式-分组范围
data_overview_image_style1 = ('xpath', "//p[text()='分组范围']")
# 可视化：样式保存按钮
data_overview_image_save = ('xpath', "//div[@class='flex-end btn']//span[text()='保存']")
# 可视化：样式保存成功提示语
data_overview_image_save_mes = ('xpath', '//p[@class="el-message__content"]')
