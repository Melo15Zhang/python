import math

print(abs(100))
print(abs(-100))
print(max(10,9,22,83))
print(int("10"))
print(float('12.34'))
print(bool(1))
print(str(100))

n1 = 10
print(hex(n1))


def my_abs(number):
    if number > -1:
        return number
    else:
        return -number


def my_abs_1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))
print(my_abs(-1))
# print(my_abs(-10))
# print(my_abs_1(-10.0))
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0


def quadratic(a, b, c):
    det = math.sqrt(b*b-4*a*c);
    num_1 = (-b + det) / (2 * a);
    num_2 = (-b - det) / (2 * a);
    return num_1, num_2


print(quadratic(4, 0, -1))
print(quadratic(2, 3, 1) == (-0.5, -1.0))
print(quadratic(2, 3, 1) == (-1.0, -0.5))

# 默认参数可以简化函数的调用,但是要注意以下几点
# 必选参数在前


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print("4的平方 =", power(4))
print("4的立方 =", power(4, 3))

# 定义默认参数要牢记一点：默认参数必须指向不变对象！


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())

print(add_end())


# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# def calc(numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n * n
#    return sum


# print(calc([1, 2, 3]))
# print(calc((1, 3, 5, 7)))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc())
print(calc(1, 3, 5, 7))

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

L = (1, 2, 3)
L_ = [1, 2, 3,4]

print(calc(*L))
print(calc(*L_))


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print(f1(1, 2))

print(f1(1, 2, c=3))

print(f1(1, 2, 3, 'a', 'b'))

print(f1(1, 2, 3, 'a', 'b', x=99))

print(f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

print(f1(*args, **kw))


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

person('Jack', 24, job='Engineer')

