# I want to create a set and allow the user to enter 5 numbers.
# Only unique numbers should be stored.
# Finally, I want to display the set.


setlist = set()   # create empty set

a= 5  # max elements allowed

print("you can enetr only the ",a, "unique numbers:")


for i in range(a):
    numbers = int(input('enetr the number: '))
    setlist.add(numbers)



print("The set is full with", a, "elements.")
print("the setlist numbers are: ", setlist)