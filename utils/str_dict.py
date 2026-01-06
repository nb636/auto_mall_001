import json


class StrDict:
    def str_to_dict(s:str)->dict:
        dict_value = json.loads(s)
        return dict_value