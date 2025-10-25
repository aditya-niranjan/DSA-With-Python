nums = [5,10,-3,-1,-10,6]

n = len(nums)
result=[0] * n
pos = 0
neg = 1
for i in range(0,n):
    if nums[i] >= 0:
        result[pos] = nums[i]
        pos+=2
    else:
        result[neg] = nums[i]
        neg+=2
        
print(result)
# Output: [5, -3, 10, -1, 6, -

