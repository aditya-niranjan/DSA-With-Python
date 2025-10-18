
#oprimal solution this is the best optimal there is no other exists neathere then this 
# time complexity  = O(N)
# space complexity = O(N)

def TwoSum(nums,target):
    n = len(nums)
    hash_map = {}

    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
           return [hash_map[remaining],i]
        hash_map[nums[i]]=i

nums = [5,9,1,2,4,15,6,3]
target = 13
result = TwoSum(nums,target)
print(result)