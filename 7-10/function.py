#!/usr/bin/python3
# Filename:function.py

import math


def print_calc(num):
    print(num ** 2)


table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}

for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))


str = input("请输入：");
print("你输入的内容是: ", str)

