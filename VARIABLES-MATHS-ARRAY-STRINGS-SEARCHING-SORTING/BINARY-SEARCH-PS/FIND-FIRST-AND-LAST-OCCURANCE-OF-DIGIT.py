
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


def Upper_Bound(nums,target):
    n = len(nums)
    upper_bound = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>target:
            upper_bound = mid
            high= mid-1
        else:
            low = mid + 1
    return upper_bound - 1

nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = int(input("Enter the target value to find Lower Bound: "))
print(Lower_Bound(nums,target),Upper_Bound(nums,target))