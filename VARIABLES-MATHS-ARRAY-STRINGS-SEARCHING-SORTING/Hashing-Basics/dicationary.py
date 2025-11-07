n = [5,3,2,2,1,5,5,7,5,10]

m = [10,111,1,9,5,67,2]


hash_map = {}  # this is a dicationary {} or dicat() both are same

for i in range(0,len(n)):
  if n[i] in hash_map:
    hash_map[n[i]]+=1
  else:
    hash_map[n[i]]=1
 
# print(hash_map)

for num in m:
  if num in hash_map:
    print(hash_map[num],end=" ")
  else:
    print(0,end=" ")