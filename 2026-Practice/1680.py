


MOD = 10**9 + 7
n = int(input())
result = 0
length = 0


for i in range(1, n + 1):
    # if i is power of 2
    if (i & (i - 1)) == 0:
        length += 1
    result = ((result << length) + i) % MOD
print(result)

