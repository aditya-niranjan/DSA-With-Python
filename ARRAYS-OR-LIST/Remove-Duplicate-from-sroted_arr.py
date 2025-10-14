

def Remove_Duplicates_from_arr(nums):
    n = len(nums)
    i = 0
    j = i+1
    
    if n == 1:
        return 1
    
    for i in range(0,n):
        if nums[i] != nums[j]:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
        j+=1
    return i + 1

result = Remove_Duplicates_from_arr([1,1,1,2,3,4,4,7,9,9,9,10])

print(result)
      
        