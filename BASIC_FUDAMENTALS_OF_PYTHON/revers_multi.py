# DIFFRENT METHODS TO PRINT THE REVESED MULTIPLICATION OF THE NUMBER THAT IS TAKEN 
# BY FROM AN USER WITH THE HELP OF INPUT FUNCTION

n = int(input("Enter a number to get reverse multiplication: "))


# for i in range(1,11):
#   print(f"{n} x {i} = {n * i}")


# table = []


# for i in range(1,11):
#  table.append(f"{n} x {i} = {n * i}")



# for tablelist in reversed(table):
#     print(tablelist)


i = 11

while i>= 1:
    print(f"{n} x {i-1} = {n * (i-1)}")
    i -= 1
    if i == 0:
        print("End of reverse multiplication table.")
        break