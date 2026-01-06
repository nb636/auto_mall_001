import os
import allure
import pytest

from apis.login_api import LoginApi
from config import datas_path
from utils.read_excle import ReadExcel
from utils.assert_util import AssertUtil
from utils.str_dict import StrDict

datas = ReadExcel.read_excle(os.path.join(datas_path, 'data.xlsx'), 'login_datas')


@allure.feature("登录模块")
@allure.story("登录功能")
class TestLogin:
    @pytest.mark.parametrize("title,datas,statues,code,msg", datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, title, datas, statues, code, msg, get_logger):
        get_logger.info("开始执行用例")

        with allure.step("登录"):
            login_data = StrDict.str_to_dict(datas)

            res = LoginApi.login(login_data)

        with allure.step("断言"):
            AssertUtil.assert_result(res, statues, code, msg)