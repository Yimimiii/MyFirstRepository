# 每次登录后更新token，再将其存放到专门缓存的py文件中
import json

import allure
import pytest

from utils.api import APICLASS
from config.baseurl import *

api = APICLASS()

@pytest.fixture(scope = "session")  #作用域设置成session 整个会话过程中都是同一个值
@allure.title("登录接口")
def get_token():
    # global alljson_var
    # alljson_var = {}
    loginyaml = api.read_yaml("G:/Practice_items/EcommercePytestProject/testdata/login.yaml")
    logindata = loginyaml[0]
    res = api.send_request(method='post', headers=logindata['A05_header'], url=URL+logindata['A03_url'], params=logindata['A04_param'], data=logindata['A06_data'])
    # 这里模拟实现登录接口并获取 token 的过程
    resdate = json.loads(res.text)
    api.get_jsonpath(resdate, logindata['A10_jsonpath'], logindata['A11_pathexpr'], alljson_var)
    print("11111fixture函数中的token=", alljson_var['VAR_TOKEN'])
    token = alljson_var['VAR_TOKEN']

    return token





