nums = [5,-2,3,9,0,6,10,7]
k = 3
n = len(nums)
rotations = k % n


for _ in range(0,rotations):
  e = nums.pop()
  nums.insert(0,e)

print(nums, f"total rotations is : {rotations}")