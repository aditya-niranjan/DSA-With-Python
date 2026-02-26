arr = [1,2,1,4]

def threeSumClosest(arr, target):
  
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                sum = arr[i] + arr[j] + arr[k]
                if sum == target:
                    return sum
                elif sum < target:
                    closest = sum
                else:
                    closest = sum
        
    return closest


print(threeSumClosest(arr, 6))