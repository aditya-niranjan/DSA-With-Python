

#linear Search 

def LinearSearch(nums,target):

  for i in range(len(nums)+1):
    if nums[i] == target:
        return i
    else:
       i+=1

  return -1

nums = [5,3,9,8,1,6,4,-10,-100]
target = 4
result = LinearSearch(nums,target)
print(result)
  




