import sys
# start 1-100累加求和
sum = 0

for l in range(101):
    sum += l

print("sum =", sum)
# end 1-100累加求和

# start 去除1-100中整除10的数字，累加求和
list = []
int = 100
while True:
    if int < 1:
        break
    if int % 10 == 0:
        int -= 1
        continue
    list.append(int)
    int -= 1

sum = 0;
for l in list:
    sum += l;
# end去除1-100中整除10的数字,累加求和
print("sum =", sum)
