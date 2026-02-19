

n = int(input("Enter the number: "))

i = 0

while(i < n+1):
    print(" " * (i),end="")
    print(" *" * (n-i))
    i+=1