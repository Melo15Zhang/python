# 打开一个文件
f = open("/foo.txt", "r", encoding='utf-8')

str = f.read()
print(str)

# 关闭打开的文件
f.close()
# --------------------------------
# 打开一个文件
f1 = open("/foo.txt", "r", encoding='utf-8')

str1 = f1.readline()
print(str1)

# 关闭打开的文件
f1.close()
# --------------------------------
# 打开一个文件
f2= open("/foo.txt", "r", encoding='utf-8')

str2 = f2.readlines()
print(str2)

# 关闭打开的文件
f2.close()
# --------------------------------
# 打开一个文件
f = open("/foo.txt", "r", encoding='utf-8')

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()


# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后,
# 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:

with open('/foo.txt', 'r', encoding='utf-8') as f:
    read_data = f.read()
    print(read_data)

# python的pickle模块实现了基本的数据序列和反序列化
