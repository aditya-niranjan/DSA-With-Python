arr = [1, 2, 2, 3, 4, 4, 5]

k = 1

for i in range(1, len(arr)):
    if arr[i] != arr[k - 1]:
        arr[k] = arr[i]
        k += 1

print(arr[:k])