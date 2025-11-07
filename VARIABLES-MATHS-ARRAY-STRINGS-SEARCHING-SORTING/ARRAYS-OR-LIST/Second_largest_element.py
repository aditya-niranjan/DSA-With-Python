

nums = [55,34,88,99,12,98,23,67,3]

n = len(nums)

largest = float("-inf")
Second_laregest = float("-inf")

for i in range(0,n):
  if nums[i] > largest:
      Second_laregest = largest
      largest = nums[i]
  elif nums[i] > Second_laregest and nums[i] != largest:
     Second_laregest = nums[i]
print(Second_laregest)