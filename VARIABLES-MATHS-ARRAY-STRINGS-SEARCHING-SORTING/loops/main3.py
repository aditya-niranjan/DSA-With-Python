class Solution(object):
    def twoSum(self, nums, target, start, end):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff],i]
            d[num] = i

        return []

s1 = Solution()
print(s1.twoSum([2,7,11,15],9,0,1))
print(s1.twoSum([3,2,4],6,0,1))
print(s1.twoSum([3,3],6,0,1))