


n  = int(input("ENter the number"))

for row in range(n):
  for col in range(n):
    if row == n-1 or col == row or col == 0:
      print("*",end="")
    else:
      print(" ",end="")
  print()