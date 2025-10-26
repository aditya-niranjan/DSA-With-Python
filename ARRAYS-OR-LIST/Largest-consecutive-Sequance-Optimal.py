nums = [1,99,101,98,2,5,3,100,1,1]

n  = len(nums)
my_set = set()

for i in range(0,n):
  my_set.add(nums[i])

logest = 0

for num in my_set:
  if num-1 not in nums:
    x = num
    count = 1
    while x+1 in my_set:
      count+=1
      x+=1
    logest= max(logest, count)

print(logest)