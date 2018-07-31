#!/usr/bin/python3

# 可写函数说明
sum = lambda arg1, arg2: arg1 * arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


g= lambda x=0,y=0 : x**2+y**2
print("g(2,3) -->" ,g(2,3));
print("g(2) -->" ,g(2));
print("g(y=3) -->" ,g(y=3));