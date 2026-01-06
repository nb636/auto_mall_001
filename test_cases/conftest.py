import pytest
import requests

from utils.log_util import LogUtil


@pytest.fixture(scope="class")
def get_logger():
    logger = LogUtil.get_logger()
    yield logger

@pytest.fixture(scope="function")
def login():
    data = {
        'username': 'admin',
        'password': 'macro123'
    }
    res = requests.post(url='https://admin-api.macrozheng.com/admin/login', json=data)
    a=res.json().get("data").get('tokenHead')
    b=res.json().get("data").get('token')
    token = a + b
    yield token