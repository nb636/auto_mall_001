import requests
url = "https://admin-api.macrozheng.com/admin/login"
class LoginApi:
    @classmethod
    def login(self,login_data):
        res = requests.post(url, json=login_data)
        return res