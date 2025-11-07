
def MaximumSubArray(numas):
    n = len(nums)
    total  = 0
    maxi = float("-inf")
  
    for i in range(0,n):
        total = 0
        for j in range(i,n):
            total+=nums[i]
            maxi = max(maxi,total)
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]

result = MaximumSubArray(nums)
print(result)