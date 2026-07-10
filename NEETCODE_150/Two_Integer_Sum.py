
numbers = [1,2,3,4]
target = 3

# result = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if  nums[i] + nums[j] == target and i < j:
#           result.append([nums[i],nums[j]])
        

# return result


def fun(nums,target):

  left = 0 
  right = len(nums)-1

  while left < right:
      if nums[left] + nums[right] > target:
        right-=1
        left+=1
        continue
      
      if nums[left] + nums[right] == target  and nums[left] < nums[right]:
        return [nums[left],nums[right]]

      return -1
print(fun(numbers,target))







                
