#Bubble sort with best case optimization 

def BubbleSort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
       is_swap = False
       for j in range(0,i+1):           
           if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swap =True

       if is_swap == False:
            print("List Is Already Sorted Only")
       return nums
n = [1,2,3,4,5,6,7,8,9,10]
# print(n)
result = BubbleSort(n)
print(result)
