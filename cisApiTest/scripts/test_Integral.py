"""
description: 积分管理接口测试用例
time: 2022/06/14
author: chenling
"""
import json
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
import api_config

@allure.feature("积分管理模块")
class TestIntegral:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\Integral.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("我的积分菜单")
    @allure.severity("NORMAL")
    @allure.description("我的积分查询")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "我的积分", None, 1, 2, 3, 4, 7, 8, 9))
    def test_myIntegral_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))

        res_text = ApiFactory.get_Integral().myIntegral(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
        logging.info("返回结果：{}".format(res_text.json()))
        assert_common(res_text, msg=exc_data)

    @allure.story("我的积分菜单")
    @allure.severity("NORMAL")
    @allure.description("积分详情")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "积分详情", None, 1, 2, 3, 4, 7, 8, 9))
    def test_integralPage_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))

        res_text = ApiFactory.get_Integral().integralPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
        logging.info("返回结果：{}".format(res_text.json()))
        assert_common(res_text, msg=exc_data)


