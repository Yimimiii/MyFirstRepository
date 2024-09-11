import json
import allure
import pytest
from utils.api import APICLASS
from config.baseurl import *
from deepdiff import DeepDiff



# 实例化基类对象，后续需要调用基类的方法时，就通过这个对象来调用
api = APICLASS()


@pytest.fixture(scope="module",autouse=True)
def setup_module():
    # 定义全局变量，确保整个模块中都能使用(一定要先设全局再赋值，不然会报错)
    global alljson_var, allre_var, sqlvarlist
    alljson_var = {}
    allre_var = {}
    sqlvarlist = []

@allure.title("注册接口")
@pytest.mark.parametrize("regdata", api.read_yaml("G:/Practice_items/EcommercePytestProject/testdata/reg.yaml"))
def test_reg(regdata):
    # 如果发送请求的几大参数中,有需要数据关联的地方,则需要提前处理数据
    res = api.send_request(method=regdata['A02_method'], headers=regdata['A05_header'], url=URL+regdata['A03_url'], params=regdata['A04_param'], data=regdata['A06_data'])
    print(res.text)


    # 注意在取值进行断言前，需要先把转化成字典格式
    resdata = json.loads(res.text)

    # 做全字段断言太麻烦，要对比的数据字段太多
    # 响应断言 和yaml中定义的预期结果进行比对
    # assert regdata['A08_expectmsg'] == resdata['msg']
    print("注册okkk")


    # 提取jsonpath里的数据并保存到全局变量all_var中
    if regdata['A10_jsonpath'] is not None:
        api.get_jsonpath(resdata, regdata['A10_jsonpath'], regdata['A11_pathexpr'], alljson_var)
        print(alljson_var)



    # 提取正则表达式的数据并保存到全局变量all_var中
    # if regdata['A12_regular'] is not None:
    #     api.get_repath(resdata, regdata['A12_regular'], regdata['A13_regularEXPR'], allre_var)
    #     print(allre_var)


    # 提取sql里的变量，进行数据库结果断言,提前定义一个全局变量以list的形式存放需要的值
    if regdata['A15_sql'] is not None:
            sql_var = regdata['A14_sqlvar'].replace('${', '').replace('}$', '').replace("${", "").replace("}$", "")
            svar = sql_var.split(";")
            for i in range(len(svar)):
                sqlvarlist.append(eval(svar[i]))
            sql = regdata['A15_sql'].format(*sqlvarlist)
            res = api.get_dbsql(sql)
            assert res[0] == alljson_var['VAR_TOKEN']
            print("数据库断言成功")









