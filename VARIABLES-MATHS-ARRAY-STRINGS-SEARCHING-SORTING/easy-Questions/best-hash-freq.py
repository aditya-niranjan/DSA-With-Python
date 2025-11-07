

def frequncey(n):
  nums = n
  hash_map = {}
  for i in range(0,len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
  
  return hash_map
n = [5, 2, 2, 1, 5, 3, 4, 1, 6, 7, 8, 5, 3, 2, 1,1,1,1,1,1,1,1,1]
result = frequncey(n)
print(result)
