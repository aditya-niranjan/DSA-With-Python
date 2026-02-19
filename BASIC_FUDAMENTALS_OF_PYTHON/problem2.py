import random

setlist = set()
a = 10


attempts = 0
while len(setlist) < a and attempts < 10:  # limit attempts to prevent infinite loop
    num1 = random.randint(0, 100)* 2
    num2 = random.randint(0,100)* 2

    print("the num1 is:", num1)
    print("the num2 is:", num2)

    if num1 == num2:
        setlist.add(num1)
        attempts += 1


print("The set of unique even numbers (with matched pairs) is:", setlist)
