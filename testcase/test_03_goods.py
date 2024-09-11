import json

import jsonpath
import pytest

from config.baseurl import *
from utils.api import APICLASS
from config.cachetoken import get_token

api = APICLASS()

@pytest.mark.parametrize("goodsdata", api.read_yaml("G:/Practice_items/EcommercePytestProject/testdata/goods.yaml"))
# @pytest.mark.run(order=1)
def test_goods(get_token, goodsdata):
    # 通过fixture函数获取token
    # print("AAAAAAAAAAAAAA", get_token)
    # 将token加到请求的公共参数中
    # print(goodsdata)
    # print(type(goodsdata))
    params = goodsdata['A04_param']
    # print(type(params))
    # print(params)

    # 如果需要传入token的接口，就进行下面步骤将token传进去
    if 'token' in params:
        params['token'] = get_token

    # 请求参数，传递到发起请求的接口中
    data = goodsdata['A06_data']

    # 请求参数数据，有些是从上一个接口中提取的，就想要进行以下操作
    if goodsdata['A06_data'] is not None:
        print(type(goodsdata['A06_data']))
        data = str(goodsdata['A06_data']).replace('"${', '').replace('}$"', '').replace("'${", "").replace("}$'", "")
        print("2222有没有实现str字符串的转换？？？")
        print(eval(data))
        data= eval(data)
        print("2有没有实现str字符串的转换？？？")
        print(data)



    res = api.send_request(method=goodsdata['A02_method'], headers=goodsdata['A05_header'], url=URL + goodsdata['A03_url'],params=goodsdata['A04_param'], data=data)
    # print(res.text)
    # print(type(res.text))
    resdate = json.loads(res.text)
    # print(type(resdate))

    if goodsdata['A10_jsonpath'] is not None:
        print("33333存放提取的所有值的list=", api.get_jsonpath(resdata=resdate, jsonpathstr1=goodsdata['A10_jsonpath'], jsonpathstr2=goodsdata['A11_pathexpr'], alljson_var=alljson_var))

    print('44444请求参数data=', data)
