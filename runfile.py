
# 需要从主入口那里运行的测试文件
import glob

# 文件夹名称
folder_path ='G:/Practice_items/EcommercePytestProject/testcase'
# 匹配需要执行的文件的匹配模式，这个表示在上面的文件夹目录下取所有以py结尾的文件来运行
file_pattern ='*.py'

test_files = glob.glob(f"{folder_path}/{file_pattern}")
