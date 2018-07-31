# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


d = {"Michael": "95", "Bob": 75, "Tracy": 85}
print(d["Michael"])

if "Job" in d:
    print("Job key is exists")
else:
    print("Job key is not exists")

# 如果key不存在，返回None
if d.get("Job", -1) != -1:
    print("Job key is exists")
else:
    print("Job key is not exists")

# pop对应的key
print(d.pop("Bob"))

s = set([1, 2, 3])
s.add(4)
s.add(4)
s.add(5)
s.add(3)

s1 = s & set([1, 2, 8,6])
print("s items ")
for s_ in s:
    print(s_)
print("s1 items ")
for s_ in s1:
    print(s_)

s_1 = set([1, 2, 3])
# set 不可变
# error
# s_2 = set(1, [2, 3])

for s_ in s_1:
    print(s_)
# for s_ in s_2:
#    print(s_)
# dict的value 可变,key不可变
s_3 = {"Michael": (1, 2, 3)}
# error
# s_4 = {(1, [2, 3]): "Michael"}
s_4 = {"Michael": (1, [2, 3])}

for s_ in s_3:
    print(s_3.get(s_))
for s_ in s_4:
    print(s_4.get(s_))

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(oct(18));

# 字典是支持无限极嵌套的

cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}

for i in cities['北京']:
    print(i)


for i in cities['北京']['海淀']:
    print(i)