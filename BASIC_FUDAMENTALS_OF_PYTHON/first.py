import pyjokes

joke = pyjokes.get_joke()


a  = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a == b:
    print("The numbers are equal.", joke)
else:
    print("The numbers are not equal."10)