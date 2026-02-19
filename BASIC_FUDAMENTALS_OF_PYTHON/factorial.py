from itertools import product


n = int(input("Enter a number to find Factorial: "))


# i = 1

# product = 1

# for i in range(i, n+1):
#     product = product * i

# print(f"The factorial of {n} is {product}")


# Factorial using while loop


i = 1

product = 1

while(i<=n):
    product = product * i
    i += 1
print(f"The factorial of {n} is {product}")