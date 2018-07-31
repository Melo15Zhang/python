# -*- coding: utf-8 -*-

number = 100

if number > 50:
    print("number is", number)
else:
    print("number abs is ", -number)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')



height = 1.75
weight = 80.5

BMI = weight / (height * height)
# python的链式比较简化
if BMI<18.5:
    print("体重过轻")
elif 18.5 <= BMI < 25:
    print("体重正常")
elif 25 <= BMI < 28:
    print("体重过重")
elif 28 <= BMI < 32:
    print("体重肥胖")
elif BMI >= 32:
    print("体重严重肥胖")

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')