arr = [5, 3, 4, 7, 2, 3, 5, 2]




def fun(arr):
  
  lenght = len(arr)
  for i in range(len(arr)):
      for j in range(i+1,len(arr)):
          if arr[i] == arr[j]:
             return arr[j]

print(fun(arr))