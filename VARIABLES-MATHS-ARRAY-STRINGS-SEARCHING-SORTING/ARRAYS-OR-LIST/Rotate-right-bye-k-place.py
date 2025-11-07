nums= [5,-2,3,9,0,6,10,7]
print(id(nums))
n = len(nums)-2
temp = nums[-1]

for i in range(n,-1,-1):
  nums[i+1] = nums[i]
nums[0] = temp

print(nums, id(nums))
