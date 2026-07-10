
# strs = ["act","pots","tops","cat","stop","hat"]


# chars = {}

# for chr in strs:
#     sorted_str = ''.join(sorted(chr))
#     chars[chr] = sorted_str

# print(chars)



# nums = [1,2,2,3,3,3]
# hash = {}
# for num in nums:
#     if num in hash:
#         hash[num]+=1
#     else:
#         hash[num] = 1

# k = 2
# result = []
# for key, value in hash.items():
#     if key >= k:
#         result.append(key)
        

# print(result)

from re import X


n = 10203004

n = str(n)

summ = 0
X = 0
for i in range(len(n)):
    if n[i] != '0':
        summ += int(n[i])
        X = X * 10 + int(n[i])

print(summ)
print(X)

result = 0