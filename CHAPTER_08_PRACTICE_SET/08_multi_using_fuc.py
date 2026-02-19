


n = int(input("Enter a number: "))

def multiplication(n):
    i  =  1
    while i <=10:
        print(f"{n} x {i} = {n * i}")
        i += 1
    return n

result = multiplication(n)

print(f"Multiplication table of {result}:")