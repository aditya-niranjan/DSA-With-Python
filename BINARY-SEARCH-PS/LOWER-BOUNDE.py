# BINARY Search using the Recursion 

def Lower_Bound(nums,target):
    n = len(nums)
    lower_bound = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2

        if nums[mid]>=target:
            lower_bound = mid
            high= mid-1
        else:
            low = mid + 1
    return lower_bound

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = int(input("Enter the target value to find Lower Bound: "))
print(Lower_Bound(nums,target))