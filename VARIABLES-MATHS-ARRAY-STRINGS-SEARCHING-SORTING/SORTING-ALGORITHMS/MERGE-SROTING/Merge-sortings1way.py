
import random

arr = [random.randint(1, 100) for _ in range(20)]

def Merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = Merge_sort(left)
    right = Merge_sort(right)

    return Merge_Array(left,right)

def Merge_Array(left ,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)

    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

result = Merge_sort(arr)
print(result)

