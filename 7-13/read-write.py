# 执行完自动close，避免忘记关闭文件导致资源的占用。

# 写
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("test")
# 读
with open('test.txt', 'r', encoding='utf-8') as f:
    str = f.readlines()
    print(str)

# 执行完自动close，避免忘记关闭文件导致资源的占用。
