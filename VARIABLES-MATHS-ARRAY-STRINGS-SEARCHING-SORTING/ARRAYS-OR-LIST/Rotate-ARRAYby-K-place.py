nums= [5,-2,3,9,0,6,10,7]

nums[:] = [nums[-1]] + nums[0:-1]

print(nums)


# nums= [5,-2,3,9,0,6,10,7]

# nums[:] = nums[-1:] + nums[:-1]

# print(nums)