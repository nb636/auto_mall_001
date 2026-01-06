class AssertUtil:
    @staticmethod
    def assert_result(res,status=None,code=None,msg=None):
        if status is not None:
            assert res.status_code==status
        if code is not None:
            assert res.json().get("code")==code
        if msg is not None:
            assert msg in res.json().get("message")
