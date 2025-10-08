from math import *



def countingDigits(n):
  num = n 
  return int(log10(num)+1)


n = 5438
result = countingDigits(n)
print(f"this the total digits: {result}")