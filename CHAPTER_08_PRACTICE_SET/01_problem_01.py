

import re


a = int(input("Enter first number: "))

b = int(input("Enter first number: "))

c = int(input("Enter first number: "))


def gretestof_three_numbers(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  elif c>a and c>b:
    return c
  else:
    return "all number are equal"
  
print(gretestof_three_numbers(a,b,c))