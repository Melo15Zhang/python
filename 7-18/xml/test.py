#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob1',
    'url' : 'http://www.runoob.com1'
}

data2 = {
    'no' : 2,
    'name' : 'Runoob2',
    'url' : 'http://www.runoob.com2'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)


# 写入 JSON 数据
with open('test.json', 'w+') as f:
    json.dump(data1, f)

