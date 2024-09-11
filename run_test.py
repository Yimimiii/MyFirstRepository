# 运行测试脚本的入口文件
import glob
import os
import shutil
import subprocess

from config.cachetoken import *
from config.baseurl import *
from runfile import test_files

# 写一个删除allure之前的报告的方法，在每次运行前删掉之前的测试报告
def delete_allure_report(directory_path,report_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        shutil.rmtree(report_path)
        print(f"目录 {directory_path} 已删除")
    else:
        print(f"目录 {directory_path} 不存在")

if __name__ == '__main__':

    delete_allure_report('G:/Practice_items/EcommercePytestProject/results/allure_report' , 'G:/Practice_items/EcommercePytestProject/allure_report')

    pytest.main(['-sv', '--alluredir', 'G:/Practice_items/EcommercePytestProject/results/allure_report'] + test_files)

    subprocess.run(['G:/allure-2.30.0/allure-2.30.0/bin/allure.bat', 'generate','G:/Practice_items/EcommercePytestProject/results/allure_report', '-o','G:/Practice_items/EcommercePytestProject/allure_report'])
    subprocess.run(['G:/allure-2.30.0/allure-2.30.0/bin/allure.bat', 'open', './allure_report'])


#
#
# def run_allure():
#
#
# if __name__ == '__main__':
#
#


# print("token=======", get_token)   #直接在这里取token是取不到的，但是在test的测试函数中直接传入可以取到
print("存放提取jsonpath的数据集合=======", alljson_var)


