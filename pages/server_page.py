# -*- coding: utf-8 -*-

"""
服务页面元素
"""
# 左侧工具栏:我的
ser_toolbar_my_btn= ('xpath', "//span[text()='我的']")
# 左侧工具栏:全部服务
ser_toolbar_all_ser= ('xpath', "//span[text()='全部服务']")
# 工具栏：删除按钮
ser_toolbar_delete_btn = ('xpath', '//*[@class="group-info-left flex-start"]/div[2]/div')
# 删除弹窗中的删除按钮
ser_pop_delete_btn = ('xpath',"//div[@class='service-content']//span[text()='删 除']")
# 删除成功后的提示语
ser_delete_mes = ('xpath','//p[@class="el-message__content"]')



# 服务概览:图层展开按钮
ser_overview_layer_unfold = ('css selector', '[class="head-right flex-end"] [class="el-image__inner"]')
# 服务概览:服务地址input框
ser_overview_server_value = ('xpath','//*[contains(@class,"sib-url-info-input")]/input')
# 服务概览:删除服务按钮
ser_overview_delete_server = ('xpath', '//span[text()="删除服务"]')
