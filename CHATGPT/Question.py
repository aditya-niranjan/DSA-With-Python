from numpy import maximum


arr = [42, 7, 91, 18, 56, 3, 75, 29]


def find_Small(arr):
    if not arr:
        return None  # Return None if the array is empty

    smallest = arr[0]  # Assume the first element is the smallest
    for num in arr:
        if num < smallest:
            smallest = num  # Update smallest if a smaller number is found
    return smallest  # Return the smallest number found



def find_Largest(arr):
    if not arr:
        return None  # Return None if the array is empty

    largest = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > largest:
            largest = num  # Update largest if a larger number is found
    return largest  # Return the largest number found




smallest_number = find_Small(arr)
largest_number = find_Largest(arr)

maximum_difference = largest_number - smallest_number

print(maximum_difference)