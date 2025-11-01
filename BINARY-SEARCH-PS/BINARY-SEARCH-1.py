
# this what the Binary search is the best for the sorted questions

def BinaraySearch(nums,target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <=  high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1        

nums = [2,3,4,5,6,7,9,10,11,12,13]
target = 12
print(BinaraySearch(nums,target))