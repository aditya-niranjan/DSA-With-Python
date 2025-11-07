class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_op = 0    
        
        while nums:

            while nums[0] != min(nums):
                nums.append(nums.pop(0))
                total_op+=1
                
            nums.pop(0)
            total_op+=1

        return total_op

s1 = Solution()
n = [3,4,-1]
result = s1.countOperationsToEmptyArray(n)
print(result)
