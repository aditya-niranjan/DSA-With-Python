

def moveZeros(nums):
  i = 0
  
  if len(nums) ==1:
    return

  while i<len(nums):
    if nums[i] == 0:
      break
    i+=1
  
  if i == len(nums):
      return
  
  j = i+1

  while j < len(nums):
      if nums[j] != 0:
         nums[i],nums[j] = nums[j],nums[i]
         i+=1
      j+=1
  
nums = [1,2,0,4,3,0,0,3,5,1]
moveZeros(nums)
print(nums)