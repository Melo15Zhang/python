import collections

classmates = ('Michael', 'Bob', 'Tracy')

print(classmates)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print("----------use index----------")
# print Apple
print(L[0][0])
# print Python
print(L[1][1])
# print Lisa
print(L[2][2])

print("----------use loop-----------")
for var in (0, 1, 2):
    print(L[var][var])

# two ways to define the field name for namedtuple

# User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', 'name age id')
user = User('tester', '22', '464643123')

print(user)