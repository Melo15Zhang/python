# 打开一个文件
f = open("/foo.txt", "w", encoding='utf-8')
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
char = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print("write char num {}".format(   char))
# 关闭打开的文件
f.close()

