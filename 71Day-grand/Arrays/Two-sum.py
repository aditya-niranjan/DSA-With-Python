




def Twosum(arr,target):

  num = len(arr)
  for i in range(num):
    for j in range(i+1,num):
      total = arr[i] + arr[j]
      if total ==target:
        return [i,j]









array = [3,2,4]
target = 6
result = Twosum(array,target)
print(result)