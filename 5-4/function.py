#!/usr/bin/python3


def ChangeInt(a):
    c = a
    c = 10


b = 2
ChangeInt(b)
print(b)


# 结果是 2


# 可写函数说明
def changeme(mylist):
    newList = mylist
    # "修改传入的列表"
    newList.append([1, 2, 3, 4])
    print("函数内取值: ", newList)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)