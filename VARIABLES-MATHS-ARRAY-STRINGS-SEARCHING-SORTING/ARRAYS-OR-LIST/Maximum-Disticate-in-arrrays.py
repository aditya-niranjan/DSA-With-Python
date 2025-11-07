




def maxDistance(arrays):
  
  min_so_far = arrays[0][0]
  max_so_far = arrays[0][-1]
  max_disticte = 0


  for i in range(1,len(arrays)):
      current = arrays[i]

      max_disticte = max(
          max_disticte,
          abs(current[-1] - min_so_far),
          abs(max_so_far - current[0])
      )

      min_so_far = min(min_so_far,current[0])
      max_so_far = max(max_so_far,current[-1])

  return max_disticte
arrays = [ [1, 2, 3], [4, 5], [1, 2, 3] ]
result = maxDistance(arrays)
print(result)