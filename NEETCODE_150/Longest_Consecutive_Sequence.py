nums1 = [2,20,4,10,3,4,5]
nums2 = [0,3,2,5,4,6,1,1]


def fun(nums):
    nums.sort()
    uni = set()
    for i in range(len(nums)):
      idx = i
      for j in range(i+1,len(nums)):
        if nums[j] - nums[idx] == 1:
            uni.add(nums[i])
            uni.add(nums[j])
            idx = j
    return len(uni)


print("this is for num1: ",fun(nums1))
print("this is for num2: ",fun(nums2))


