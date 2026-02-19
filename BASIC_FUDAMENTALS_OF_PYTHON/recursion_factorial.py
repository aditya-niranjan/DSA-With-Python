


def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return n * factorial(n-1)


n = int(input("Enter a number to calculate its factorial: "))
print(f"this is the factorial of the give number is: {factorial(n)}")