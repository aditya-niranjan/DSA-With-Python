
# this the best and optimized approach to find the factors of a number
# time complexity: O(sqrt(n))
# space complexity: O(n)


from math import sqrt
n = 36

num = n

result = []

for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
result.sort()
print(result)