import requests

url = "https://admin-api.macrozheng.com/admin/list?pageNum=1&pageSize=10&keyword=订单"
class SearchAPI:
    @classmethod
    def search(cls,token):
        headers = {"authorization":token}
        data = {
            'pageNum':1,
            'pageSize':10,
            'keyword':"订单"
        }
        res = requests.get(url=url,headers=headers,json=data)
        return res
