number = 100
number_ = 100.00
# 打印特殊字符 使用转义字符\来标识
number__ = "I\'m OK\n换行"
number__ = 'I\'m \"OK\"!\n换行'
print("number is ", number)
print("number_ is ", number_)
print("number__ is ", number__)

'''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
'''

# Python还允许用r''表示''内部的字符串默认不转义

print(r"\\\\fasfasd\\a\\")

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
... line2
... line3''')

print(r'''hello,\n
world''')

print(True and False)
print(True and not False)
print(3 >= 4)
# python中特殊的空值 不是0
var = None
print(var)

PI = 3.1415926
print(PI)

var_ = 10 / 3
var_1 = 10 % 3
var_2 = 10 // 3
print("var_=", var_)
print("var_1=", var_1)
print("var_2=", var_2)
# print(help(max))

var_4 = 4 + 4j;

print(type(var_4));

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(5 ** 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串