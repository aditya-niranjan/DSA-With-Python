

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = []

for number in list_of_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

sum_of_even_numbers = sum(even_numbers)

print("Sum of all even numbers:", sum_of_even_numbers)