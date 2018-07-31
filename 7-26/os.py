import os


def view_dir(path='d:/'):
    """
    这个函数打印给定目录中的所有文件和目录
    :args path: 指定目录，默认为当前目录
    """
    names = os.listdir("/workpython")

    print(names)