
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(4,'A','B','C')


def fact(n):
    if n==1:
      return 1
    return n * fact(n - 1)


print("5! = ", fact(5))
print("100! = ", fact(20))

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
