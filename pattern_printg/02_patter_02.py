
from token import RPAR


n = int(input("Enter the value: "))

for i in range(n):
    print(" " * i,end="")
    print("*" * (n-i))
  