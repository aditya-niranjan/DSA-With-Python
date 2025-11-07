
from pyparsing import nums


def BubbleSort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
       for j in range(0,i+1):
           if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
n = [10,8,9,7,4,2,3,1,6,5]
print(n)
result = BubbleSort(n)
print(result)

# nums = [10,8,9,7,4,2,3,1,6,5]
# n = len(nums)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j] > nums[j+1]:
#               nums[j],nums[j+1] = nums[j+1],nums[j]

# print(nums)