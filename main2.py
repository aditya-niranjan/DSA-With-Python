
nums = [1, 2, 2, 3]
n = len(nums)
i=0
incresing = True
decreasing = True

while i < n -1:
  if nums[i] <= nums[i+1]:
    decreasing = False
  elif nums[i] >= nums[i+1]:
    incresing = False
  i+=1

if incresing or decreasing:
  print("Monotonic!!")
else:
  print("NOt MOnotonic!! ")