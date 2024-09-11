# 配置文件，存放各种fixture函数和hook钩子函数

import pytest as pytest
import logging


# 针对log日志的处理
# pytest 框架中的一个钩子函数,在测试用例收集完成后被调用对收集到的测试用例的名称和节点标识进行特定的编码和解码处理
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    out = yield
    res = out.get_result()
    if res.when == "call":
        logging.info(f"测试用例id{res.nodeid}")
        logging.info(f"测试结果{res.outcome}")
        logging.info(f"故障{res.longrepr}")
        logging.info(f"异常{call.excinfo}")
        logging.info("~~~~~~~~~~~~~~~~~~~~~~")