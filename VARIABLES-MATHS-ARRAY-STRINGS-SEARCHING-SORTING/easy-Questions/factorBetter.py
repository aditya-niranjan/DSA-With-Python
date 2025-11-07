
# this one of the best and easy approach to find the factors of a number

# time complexity: O(n/2)
# space complexity: O(n)

n = 36

num = n

result = []

for i in range(1,(num//2)+1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)