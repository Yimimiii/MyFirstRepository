# 所有常用的公用方法封装到这里
import json
import re

import jsonpath as jsonpath
import pymysql
import requests
import yaml

class APICLASS:

    # 读取yaml文件
    def read_yaml(self, yamlpath):
        file = open(yamlpath, 'r', encoding='utf-8')
        return yaml.load(file, Loader=yaml.FullLoader)  #FullLoader加载器

    # 将响应结果写入到一个新的yaml文件中(或许也可以直接写入到原始的文件中？)
    def write_yaml(self, response, yamlpath):
        with open(yamlpath, 'w', encoding='utf-8') as file:
            # 将数据对象 response 序列化为 YAML 格式并写入到文件对象 file 中
            yaml.dump(response, file, allow_unicode=True)  #allow_unicode=True允许YAML输出中包含Unicode字符（比如中文）

    # 发起请求，直接根据请求方式来选择使用哪一种方法，全部封装到一起即可
    def send_request(self,method, headers, url, params, data):
        # 没有请求头，表示get请求
        if method is 'get' and headers is None:
            response = requests.get(url=url)
        elif method is 'post' and headers.get('Content-Type') == 'application/json':
            response = requests.post(headers=headers, url=url, params=params, json=data)
        elif method is 'post' and headers.get('Content-Type') == 'application/x-www-form-urlencoded' or 'multipart/form-data':
            response = requests.post(headers=headers, url=url, params=params, data=data)
        elif method is 'put' and headers.get('Content-Type') == 'application/json':
            response = requests.post(headers=headers, url=url, json=data)
        elif method is 'put' and headers.get('Content-Type') == 'application/x-www-form-urlencoded' or 'multipart/form-data':
            response = requests.post(headers=headers, url=url, data=data)
        elif method is 'delete' and headers.get('Content-Type') == 'application/json':
            response = requests.post(headers=headers, url=url, json=data)
        elif method is 'delete' and headers.get('Content-Type') == 'application/x-www-form-urlencoded' or 'multipart/form-data':
            response = requests.post(headers=headers, url=url, data=data)
        return response


    # 从结果中根据jsonpath提取变量值, 字典格式的响应结果,变量名所在key,提取路径所在的key
    def get_jsonpath(self, resdata, jsonpathstr1, jsonpathstr2,alljson_var):
        # print(resdata)
        var_list = jsonpathstr1.split(";")
        expr_list = jsonpathstr2.split(";")
        length = len(var_list)
        # print(var_list, expr_list, length)
        for i in range(length):
            # print(i)
            key = var_list[i]
            # print(key)
            expr = expr_list[i]
            # print(expr)
            value = jsonpath.jsonpath(resdata, expr)   # 从res中根据表达式取值,resdata必须是字典格式
            # print(value)
            # 将对应的值赋值给对应的key，要将所有用例中提取的值都保存起来
            alljson_var[key] = value[0]
        return alljson_var


    # 从结果中根据正则表达式提取变量值, 字典格式的响应结果,变量名所在key,提取路径所在的key
    def get_repath(self, resdata, jsonpathstr1, jsonpathstr2, allre_var):
        # jsonpathstr2 从yaml中取出来的正则表达式含有特殊字符,无法在re.search中使用???
        print(jsonpathstr1)
        print(jsonpathstr2)
        # print(type(jsonpathstr2))
        # print(type(pa))
        # yaml_value = jsonpathstr2
        # special_char_pattern = r'[^\w\s]'  # 匹配非字母、数字和空格的字符
        # if re.search(special_char_pattern, yaml_value):
        #     print("包含特殊字符")
        # else:
        #     print("不包含特殊字符")
        # print("类型是否一样", type(pa) == type(jsonpathstr2))
        # print("内容是否一样", pa == jsonpathstr2)
        # print("长度是否一样", len(pa) == len(jsonpathstr2))
        # jsonpathstr2 = jsonpathstr2.strip().replace('<', '').replace('>', '').replace('"', '').replace("'", '')  # 去除两端的空格
        # print("长度是否一样", len(pa) == len(jsonpathstr2))
        pa = r'([a-fA-F0-9]{32})'
        str1 = json.dumps(resdata)   # 必须是字符串类型
        print(type(str1))
        print(str1)
        revalue=re.search(pattern=pa, string=str1)
        # 将对应的值赋值给对应的key，要将所有用例中提取的值都保存起来
        allre_var[jsonpathstr1] = revalue.group(1)
        return allre_var


    # 连接数据库
    def get_dbsql(self,sql):
        db = pymysql.connect(    #连接数据库
            host='shop-xo.hctestedu.com',
            port=3306,
            user='api_test',
            passwd='Aa9999!',
            database='shopxo_hctested',
            charset='utf8'
        )
        cmd = db.cursor()   #创建游标
        cmd.execute(sql)    #执行sql语句
        results = cmd.fetchone()    #返回sql的执行结果,是一个元组类型的对象
        db.close()           #关闭数据库
        return results

#
# def save(data):
#     jsonstr = json.dump(data, )
#     open('../testcase/data.json', 'w') as f:
#         f.
#
# def getData():
#         json.load()
#     open('../testcase/data.json', 'w') as f:
