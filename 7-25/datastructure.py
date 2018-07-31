a = [1,2,3,4,5,4]
a.remove(1)
print(a)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]) # 元素之间不相等

a=[1,2,3]
z = [x + 1 for x in [x ** 2 for x in a]] #  求a集合元素的平方+1的结果
print(z)

(x,y) = divmod(15, 2)
print((x,y))

data = {'Kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}

for x, y in data.items():
    print("key->{} : value->{}".format(x, y))

