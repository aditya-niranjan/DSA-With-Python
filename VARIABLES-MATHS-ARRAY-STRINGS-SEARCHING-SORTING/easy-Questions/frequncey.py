

def frequncey(n):
  nums = n
  freq_map = dict()

  for i in range(0,len(nums)):
    if nums[i] in freq_map:
      freq_map[nums[i]] += 1
    else:
      freq_map[nums[i]]=1

  # print(freq_map[1]) to find the specific give target frequney
  print(freq_map)

n = [5, 2, 2, 1, 5, 3, 4, 1, 6, 7, 8, 5, 3, 2, 1,1,1,1,1,1,1,1,1]
result = frequncey(n)
