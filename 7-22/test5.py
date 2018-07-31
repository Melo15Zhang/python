#!/usr/bin/python
# -*- coding: UTF-8 -*-

array = []

for i in range(9):
    l = int(input("请输入一个整数"))
    array.append(l)


def sort_(array):

    for i in range(len(array)-1):
        for j in range(len(array)-i -1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j + 1] = temp
    return array


print(sort_(array))