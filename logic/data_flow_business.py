# -*- coding: utf-8 -*-
from kew_word.kewword import WebKeys

from logic.data_business import DataBusiness


class DataFlowBusiness(WebKeys):

    def data_flow(self,brower,set_name, data_type, file_name):
        DataBusiness(brower).upload_data_business(set_name, data_type, file_name)