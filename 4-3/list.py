# list 是以[]为单位的

numberList = ["Java", "C#", "Python"]
numberList_ = [300, 1, 4454]

print(len(numberList))
print(len(numberList_))

numberList.pop()
print(numberList)

numberList_.pop()
print(numberList_)

# !/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc'];

print("A List : ", aList.pop())
print("B List : ", aList.pop(2))

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
