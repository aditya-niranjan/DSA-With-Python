
input = [10, 20, 45, 98, 99]

max_val = max(input)

second_largest = None

for num in input:
  if num != max_val:
    if second_largest is None or num > second_largest:
      second_largest =num
print(f"First largest number is:{max_val}\nSecond largest number is:{second_largest}")
