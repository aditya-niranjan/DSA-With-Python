n = int(input("Enter the value:"))

i = 0
while(i <=n):
  print(" " * (n - i + 1),end="")
  print(f"{i}" * ( 2 * i - 1 ))
  i+=1
