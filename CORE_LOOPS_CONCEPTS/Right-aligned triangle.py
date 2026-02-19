'''
    *
   **
  ***
 ****
*****


'''


# first solution 

n = int(input("Enter the number of rows: "))


for i in range(n):
    for j in range(n - i - 1):
        print(" ",end="")
    for j in range(i + 1):
        print("*", end="")
    print()

# second solution 

n2 = int(input("Enter the number of rows: "))

for i in range(n2):
    print(" " * (n2 - i - 1) + "*" * (i + 1))