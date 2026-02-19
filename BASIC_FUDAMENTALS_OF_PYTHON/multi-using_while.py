


n = int(input("Enter a number to generate its multiplication table: "))

i = 1

while (i < 11):
    result = n * i
    print(f"{n} x {i} = {result}")
    i += 1
    if i == 11:
        print("End of multiplication table.")
        break