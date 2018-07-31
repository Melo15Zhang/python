# -*- coding: utf-8 -*-
import os

# 导入os模块，模块的概念后面讲到
# loop
# 打印不换行 end=''
for x in range(1, 10):
    for y in range(1, x + 1):
        if x * y < 10:
            print(x, '*', y, "=", (x * y), '  ', end='')
        else:
            print(x, '*', y, "=", (x * y), ' ', end='')
print()

L = [d for d in os.listdir('./../')]  # os.listdir可以列出文件和目
print(L)

M = [m + n for m in range(1, 10) for n in range(1, 2)]
print(M)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
D = [k + '=' + v for k, v in d.items()]
print(D)

L_1 = [s.upper() for s in L]
print(L_1)
