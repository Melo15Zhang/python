#!/usr/bin/env python3
row = int(input("Enter the number of rows: "))

"""""""""""""""
******
*****
****
***
**
*
"""""""""""""""
n = row
while n >= 0:
    x = "*" * n
    print(x)
    n -= 1

"""""""""""""""
*
**
***
****
*****
******
"""""""""""""""
n = 1
while n <= row:
    x = "*" * n
    print(x)
    n += 1

"""""""""""""""
******
 *****
  ****
   ***
    **
     *
"""""""""""""""
n = row
while n >= 0:
    x = " " * (row-n)
    print(x, end="")
    y = "*" * n
    print(y)
    n -= 1

"""""""""""""""
     *
    **
   ***
  ****
 *****
******
"""""""""""""""
n = 1
while n <= 6:
    x = " " * (row-n)
    print(x, end="")
    y = "*" * n
    print(y)
    n += 1