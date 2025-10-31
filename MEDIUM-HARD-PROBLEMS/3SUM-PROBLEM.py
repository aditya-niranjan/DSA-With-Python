

def Three_Sum(arr):
  n = len(arr)
  my_set = set()
  for i in range(0,n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        if arr[i] + arr[j] + arr[k] == 0:
            temp = [arr[i],arr[j],arr[k]]
            temp.sort()
            my_set.add(tuple(temp))

  return [list(ans) for ans in my_set]

arr = [-1, 0, 1, 2, -1, -4]
print(Three_Sum(arr))