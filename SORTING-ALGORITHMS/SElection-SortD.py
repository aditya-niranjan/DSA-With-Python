# Selection Sort In Dcreasing Order Algorithm Implementation in Python


def SelectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] > nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
result = SelectionSort([10,8,9,7,4,2,3,1,6,5])
print(result)