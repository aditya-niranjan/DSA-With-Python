
n = int(input("Enter the numbe: "))


# for i in range(n+1):
#   print(" " * (n-i),end="")
#   print(" *" * (i))


i = 1

iterantions = 0 
while (i < n+1):
    print(" " * (n - i),end="")
    print(" *" * (i))
    i+=1
    iterantions+=1
print(f"total itretions are {iterantions}")
print("the all itreatonsa are completed guys!!!")