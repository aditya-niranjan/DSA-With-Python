
# TC ->> FOR SORTING O(N LOG N) + O(N) FOR (forloop) and constant time for conditional checking
# SC ->> IS O(1)just using bunch of constant space for variables

nums = [1,99,101,98,2,5,3,100,1,1]

nums.sort()
n = len(nums)
last_smaller = float("-inf")
count = 0
longest = 0

for i in range(0,n):
  num = nums[i]
  if num - 1 == last_smaller:
      count+=1
      last_smaller = num
  elif num != last_smaller:
      count = 1
      last_smaller = num
  longest = max(longest,count)

print(longest)
