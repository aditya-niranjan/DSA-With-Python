nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
i=0
while i<n:
  if nums[i] == 0:
    e = nums.pop(i)
    nums.append(e)
    n-=1
  else:
    i+=1

print(nums)

