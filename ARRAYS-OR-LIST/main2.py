#Find largest Elemnet in the Array

nums = [55,34,88,99,12,99,23,67,3]

n = len(nums)
largest = float("-inf")
for i in range(0,n):
  largest = max(largest,nums[i])

print(largest)
