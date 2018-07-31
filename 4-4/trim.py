def trim(s):
    while s[:1]==' ':
        s = s[1:]
    while s[-1:]==' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('fail!')
elif trim('  hello') !='hello':
    print('fail')
elif trim('  hello world  ') != 'hello world':
    print('fail')
elif trim('') != '':
    print('fail')
elif trim('       ') !='':
    print('fail')
else:
    print('success!')
		

	