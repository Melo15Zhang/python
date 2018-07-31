# !/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDays(year, month, day):
    '''
        获取一年的第几天
    '''
    daySum = 0
    if month < 0 or month >12:
        print("月份错误")
    else:
        for i in range(month-1):
            daySum += days[i]

        if isleapyear(year):
            daySum += 1

        daySum += day

        return daySum


def isleapyear(year):
    if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False


print("{} 年 {} 月 {} 日 是一年中的第{} 天".format(year, month, day, getDays(year, month, day)))