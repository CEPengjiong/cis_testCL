"""
description: 积分管理接口
time: 2022/06/14
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class Integral:

    # 我的积分菜单
    def myIntegral(self, moudle_name, case_name, request_method, url, data):

        url = url + _t

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 积分详情菜单
    def integralPage(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.week_ago) + "&endTime=" + str(api_config.today)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)