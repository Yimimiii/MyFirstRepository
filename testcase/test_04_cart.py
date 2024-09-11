import json

import pytest

from config.baseurl import *
from config.cachetoken import get_token



@pytest.mark.parametrize("cartdata", api.read_yaml("G:/Practice_items/EcommercePytestProject/testdata/cart.yaml"))
# @pytest.mark.run(order=2)
def test_cart(get_token, cartdata):
    # 这里需要商品id来加入购物车，但是从token中取到的alljson_var里面还不存在商品id，因为这里还没有实现与上一个03.py文件按顺序执行。
    # 所以暂时随便在yaml中写几个数据代替
    print("5555全局的json提取出来的数据都存放在这里", alljson_var)

    # 公共参数
    params = cartdata['A04_param']
    # print(params)

    # 如果需要传入token的接口，就进行下面步骤将token传进去
    if 'token' in params:
        params['token'] = get_token
    # print("公共参数", params)

    # 请求参数，传递到发起请求的接口中
    data = cartdata['A06_data']
    # print(data)

    # 请求参数数据，有些是从上一个接口中提取的，就想要进行以下操作
    if cartdata['A06_data'] is not None:
        print(type(cartdata['A06_data']))
        data = str(cartdata['A06_data']).replace('"${', '').replace('}$"', '').replace("'${", "").replace("}$'", "")
        data = eval(data)
        print("666666操作后的data=", data)

    res = api.send_request(method=cartdata['A02_method'], headers=cartdata['A05_header'],url=URL + cartdata['A03_url'], params=cartdata['A04_param'], data=data)
    print(res.text)
    print(type(res.text))
    resdate = json.loads(res.text)
    print(type(resdate))

    if cartdata['A10_jsonpath'] is not None:
        print("存放提取的所有值的list=", api.get_jsonpath(resdata=resdate, jsonpathstr1=cartdata['A10_jsonpath'],jsonpathstr2=cartdata['A11_pathexpr'], alljson_var=alljson_var))

    print('请求参数data=', data)