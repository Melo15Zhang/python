print("ord('A') =", ord('A'))
print("ord('中') =", ord('中'))
print("chr(66) =", chr(66))
print("chr(25991) =", chr(25991))
print("\u4e2d\u6587")
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 中文字节数超过了ascii编码范围，所以会报错
# print('中文'.encode('ascii'))
# 只有一个\
print (len("sadasdasda\\sdasd"))
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换
# %d 中的非零开头数字表示长度，如果长度不够 用0补充 不能用其他非0数字代替
# %.1f 数字1以上就保留整数 0.1即表示一位小数 %.1f
print('%03d-%.1f' % (30, 9))
# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
score1 = 72
score2 = 85

print('小明的成绩从去年的{0}分提升到了今年的{1}分,成绩提升了 {2:.1f}%'.format(score1,score2, (100 * (score2-score1) / score1)))