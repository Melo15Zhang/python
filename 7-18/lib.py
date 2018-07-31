import os
import shutil
import glob
import sys  # 命令行参数
import re  # re模块为高级字符串处理提供了正则表达式工具
import math  # math模块为浮点运算提供了对底层C函数库的访问
import random  # random提供了生成随机数的工具
from datetime import date
import doctest

print(os.getcwd())
os.chdir('D:/workpython/python/7-17/oop')
# 必须要绝对的目录路径

# os.system('mkdir test')

shutil.copyfile(os.getcwd() + '\\override.py', 'override1.py')

# shutil.move(os.getcwd() + '\\override1.py', os.getcwd() + '\\test')

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
disk_usage = shutil.disk_usage(os.getcwd())
print("disk_usage used {} GB".format(disk_usage.used / 1024 / 1024 / 1024))
print("disk_usage total {} GB".format(disk_usage.total / 1024 / 1024 / 1024))
print("disk_usage free {} GB".format(disk_usage.free / 1024 / 1024 / 1024))

# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
os.chdir('D:/workpython/python/7-17/oop/test')
# glob受到 os的chdir 方法影响 查找范围是当前的目录
print(glob.glob('*.py'))

print(sys.argv)

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print(math.factorial(5))  # 5!=120
print(math.sqrt(16))  # 16的 开方 4 返回小数

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())  # random float 0~1之间
print(random.randint(1, 100))
print(random.randrange(100))


# 直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile
# datetime模块为日期和时间处理同时提供了简单和复杂的方法
# 最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:

print(date.today())


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()   # 自动验证嵌入测试
