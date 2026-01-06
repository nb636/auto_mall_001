import allure

from apis.search_api import SearchAPI
from utils.log_util import LogUtil


@allure.feature("搜索订单信息")
@allure.story("搜索订单")
class TestSearch:
    def test_search(self,login):
        LogUtil.get_logger().info("开始搜索订单")

        with allure.step("搜索"):
            res = SearchAPI.search(login)


