
n  = int(input("Enter the number "))

for i in range(n):
  if i < n /2:
    print("*" * (i))
  else:
    print("*" * (n-i))