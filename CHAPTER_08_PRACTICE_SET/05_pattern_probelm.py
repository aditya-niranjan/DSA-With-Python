


'''

***
**
*
  *
 ***
*****


'''


n = int(input("Enter a number: "))

def pyramid(n, i=1):
    if i > n:
        return
    else:
        print(" " * (n - i) + "*" * (2 * i - 1))
        pyramid(n, i + 1)

pyramid(n)

