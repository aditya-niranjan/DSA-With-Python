

'''
sum = 1
sum = 1 + 2
sum = 1 + 2 + 3
sum = 1 + 2 + 3 + 4 
sum = 1 + 2 + 3 + 4 + 5
sum = 1 + 2 + 3 + 4 + 5 + 6
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7
sum = 1 + 2 + 3 + 4 + 5 + 6  + 7 + 8 + 9
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
'''

import re


n = int(input("Enter a number: "))

def sum(n):
  if(n==1):
    return 1
  else:
    return sum(n-1) + n
  

result = sum(n)

print(f"sum of 10 narural number is: {result}")

