#!/usr/bin/python3

# 可写函数说明  关键字参数


def printinfo(name, age):
    # "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


def printinfo_1(name, age = 35):
    # "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 可写函数说明
def printinfo_2(arg1, *vartuple):
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(name="runoob", age=50)
# 调用printinfo_1 函数
printinfo_1(name="runoob")
# 调用printinfo_2 函数
printinfo_2(10)
printinfo_2(70, 60, "asd")