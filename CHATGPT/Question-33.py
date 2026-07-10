arr = [1, 2, 4, 5, 6, 7, 8]

lenght = len(arr)+1

totalSumcurrent = 0
for i in range(len(arr)):
  totalSumcurrent+=arr[i]

totalactualSum = 0
for i in range(1,lenght+1):
    totalactualSum+=i


# print(totalactualSum)
missingnumber = totalactualSum - totalSumcurrent
print(missingnumber)