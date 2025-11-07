
def Reverse(nums,left,right):
    
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1



nums = [3,9,5,6,7,2,10,9]
n = len(nums)
k = 5
k = k % n
Reverse(nums,n-k,n-1)
Reverse(nums,0,k-n-1)
Reverse(nums,0,n-1)

print(nums)