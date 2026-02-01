
num = int(input("Enter the numbers!!"))


# for row in range(1,num+1):
#   for col in range(1,num+1):
#       if(row > col):
#          print(" ",end=" ")
#       else:
#          print(" *",end="")
#   print()

for i in range(num):
    print("  " * i + "* " * (num - i))
