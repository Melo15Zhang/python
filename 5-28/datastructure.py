#!/usr/bin/python3


# 列表的相关方法

list = []

list.append("x")

print("list.append -->{}".format(list))

list2 = ["a", "b"]

list.extend(list2)

print("list.extend {} --> {}".format(list2, list))

list.insert(1, "d")  # 参数是对应的下标

print("list.insert index {},element {} --> {}".format(1, "d", list))

list.remove("b")

print("list.remove {}-->{}".format("b", list))

a = list.pop()

print("list.pop -->{}".format(list))

# list.clear()

# print("list.clear -->{}".format(list))

# list.sort() reverse=0 表示正序asc reverse=1 表示desc 等价于list.reverse()

list.sort(reverse=0)

print("list.sort reverse = {}-->{}".format(0, list))

list.sort(reverse=1)

print("list.sort reverse = {}-->{}".format(1, list))

list.reverse()

print("list.reverse -->{}".format(list))

index = list.index('d')

print("list.index {}-->{}".format('d', index))

print("list.count {}-->{}".format('d', list.count('d')))

list3 = list.copy();

list[0] = 0  # 返回列表的浅复制 等于a[:]

print("list a[:] list-->{}".format(list))

print("list.copy list3-->{}".format(list3))

list4 = list[:]

list[0] = 1

print("list a[:] list-->{}".format(list))

print("list a[:] list4-->{}".format(list4))


# 把list当做stack用,用append 和pop方法使得列表可以很方便的作为一个堆栈来使用，
# 堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来

# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
# 用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
# 返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号


vec = [2, 4, 6]
vec_ = [3*x for x in vec]

print(vec_)

# 乘法表

result = [[x, y, x*y] for x in range(1, 10) for y in range(1, x+1)]
print(result)

for z in [[x, y, x*y] for x in range(1, 10) for y in range(1, x+1)]:
    if z[2] > 9:
        print("{} x {} = {}".format(z[0], z[1], z[2]), end=" ")
    else:
        print("{} x {} = {}".format(z[0], z[1], z[2]), end="  ")
    if z[0] == z[1]:
        print("\n")

# for x in range(1, 10):
#     for y in range(1, x + 1):
#         if x*y > 9:
#             print("{} x {} = {}".format(x, y, x*y), end=" ")
#         else:
#             print("{} x {} = {}".format(x, y, x*y), end="  ")
#         if x == y:
#             print("\n")


# 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

for f in set(basket):
    print(f)