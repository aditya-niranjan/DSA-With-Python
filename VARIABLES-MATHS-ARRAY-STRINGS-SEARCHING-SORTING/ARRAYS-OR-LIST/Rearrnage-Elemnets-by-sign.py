
nums = [5,10,-3,-1,-10,6]

n = len(nums)
positive = []
negative = []
result = []

for i in range(0,n):
  if nums[i] > 0:
    positive.append(nums[i])
  else:
    negative.append(nums[i])

for i in range(0, len(positive)):
  result.append(positive[i])
  result.append(negative[i])
 

print(result)

# Output: [5, -3, 10, -1, 6, -10]
