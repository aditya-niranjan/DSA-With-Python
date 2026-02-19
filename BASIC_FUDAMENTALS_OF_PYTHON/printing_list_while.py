


setlist = set()   # create empty set

a = 5  # max elements allowed

print("You can enter", a, "unique numbers:")

for i in range(a):
    num = int(input("Enter number: "))
    setlist.add(num)

print("The set is full with", a, "elements.")
print("The set is:", setlist)

setlist1 = {1, 2, 3, 4, 5}  # create set with initial elements
setlist2 = {1,2,3,6,7,8}  # create another set with initial elements

print("Set 1:", setlist1)
print("Set 2:", setlist2) 

print("Union of Set 1 and Set 2:", setlist1 and setlist2)  # union 

print("Intersection of Set 1 and Set 2:", setlist1 & setlist2)  # intersection

print("Difference of Set 1 and Set 2:", setlist1 - setlist2)  # difference

