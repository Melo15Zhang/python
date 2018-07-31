# -*- coding: utf-8 -*-
#d = {'a': 1, 'b': 2, 'c': 3}
#for key,value in d.items():
#	print(key,value)

# return tuple


def findMinAndMax(L):
	if len(L)==0:
		return (None,None)
	max = L[0]
	min = L[0]
	for x in L[1:]:
		if(max<x):
			max = x
		if(min>x):
			min = x
	return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')		