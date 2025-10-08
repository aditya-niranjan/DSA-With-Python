# this bruth force solution finds all the factors of a number

# time complexity: O(n)
# space complexity: O(n)

n = 36

num = n

result = []

for i in range(1,num +1):
  if num % i==0:
    result.append(i)

print(result)