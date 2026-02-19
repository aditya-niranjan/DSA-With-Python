
string1 = input("Enter a string1: ")
string2 = input("Enter a string2: ")


string1 = string1.lower()
string2 = string2.lower()


if string1 < string2:
    print("-1")
elif string1 > string2:
    print("1")
else:
    print("0")