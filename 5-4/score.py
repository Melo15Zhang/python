#!/usr/bin/python3

# 可写函数说明


def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total


# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)


# if/elif/else/、try/except、for/while等不会引入新的作用域的

if True:
    msg = "hello if/else";

print("if/else msg --> ", msg)

total = 0

# 这是一个全局变量
# 可写函数说明


def sum( arg1, arg2 ):
    # 返回2个参数的和"
    total = arg1 + arg2
    # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)