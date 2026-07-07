arr = [1, 7, 3, 6, 5, 6]


def equilibrium_index(arr):
  left  = 0
  right = 0
  for i in range(len(arr)):
    left = sum(arr[:i])
    right = sum(arr[i+1:])

    if left == right:
        return i
      
  return -1

print(equilibrium_index(arr))