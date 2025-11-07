# BINARY Search using the Recursion 

def BinaraySearch(nums,low,high,target):
    if low > high:
        return -1
    mid = (low + high)//2
    if nums[mid] == target:
          return mid
    elif nums[mid] < target:
         return BinaraySearch(nums,mid+1,high,target)
    else:
         return BinaraySearch(nums,low,mid-1,target)
nums = [2,3,4,5,6,7,9,10,11,12,13]
target = 12
print(BinaraySearch(nums,0,len(nums),target))