#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy


a = [1, 2, 3]
b = a[0:]
print(b)

a1 = [1,2,3,4,5]
b1 = ["A","B",a]
# 浅拷贝
c1 = b1[:]
print(c1)
# 此时a变化c跟着变化
a[0] = 11
print(c1)

# 深拷贝
c2 = copy.deepcopy(b1)
a1[0] = 111
print(c2)
# 此时c中数据不受a影响

