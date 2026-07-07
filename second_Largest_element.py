

arr = [8,29,176,93,84,27,2938,476,489]




maxi = 0
second = maxi
for i in range(len(arr)):
      temp = arr[i]
      maxi = max(maxi,temp)
      second = min(temp,maxi)

print(maxi)
print(second)