# 存放一些基础路径，全局变量等内容

# 基础路径，整个项目共用的
import glob

from utils.api import APICLASS

URL="http://shop-xo.hctestedu.com/index.php?s="

# 全局的alljson_var，里面存放的是所有从jsonpath中提取出来的键值对，写在这里让任何py文件都可以直接使用
alljson_var = {}

# 实例化基类的对象
api = APICLASS()
