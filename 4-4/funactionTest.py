# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def product(x, *y):
	sum = 1;
	if x is None:
		return sum
	else:
		sum = x

	for int in y:
		sum *= int
	return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
	print('测试失败!')
elif product(5, 6) != 30:
	print('测试失败!')
elif product(5, 6, 7) != 210:
	print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
	print('测试失败!')
else:
	try:
		product()
		print('测试失败!')
	except TypeError:
		print('测试成功!')