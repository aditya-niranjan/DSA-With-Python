
num1 = [1,1,1,2,4,6,7]
num2 = [1,2,3,6,7,8,9,10]

# Approach 1: Using Hashing

hash_fre = {}

for i in range(len(num1)):
    hash_fre[num1[i]]=1

for i in range(len(num2)):
    hash_fre[num2[i]]=1

print(hash_fre)

# Approach 2: Two Pointer Technique
n,m = len(num1),len(num2)
result = []
i = j = 0

while i<n and j<m:
  if num1[i] <= num2[j]:
      if len(result) == 0 or result[-1] != num1[i]:
          result.append(num1[i])
      i+=1
  else:
      if len(result) == 0 or result[-1] != num2[j]:
          result.append(num2[j])
      j+=1

while i<n:
    if len(result) == 0 or result[-1] != num1[i]:
      result.append(num1[i])
    i+=1

while j<m:
   if len(result) == 0 or result[-1] != num2[j]:
      result.append(num2[j])
   j+=1

print(result)