
# this one is Upper Bound code

# the only diffrenece in the LOWER BOUND AND UPPER BOUND CODE is that belowe see
# Lower bound the nums[mid] >= target
# Upper bound the nums[mid] > target 

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
    return upper_bound

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = int(input("Enter the target value to find Lower Bound: "))
print(Upper_Bound(nums,target))