# nums = [55,34,88,99,12,99,23,67,3]
# nums = [1,2,3,4,5,6,7,8,9]

def Sorted_or_not(nums):
    n = len(nums)
    j = 0
    for i in range(0,n):
        j = i+1
        if nums[i] > j:
            return False
        else:
            return True
      

print(Sorted_or_not([1,2,3,4,5,6,7,8,9]))