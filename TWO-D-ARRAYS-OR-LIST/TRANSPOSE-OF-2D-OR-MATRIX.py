from operator import le


matrix = [
    [5, 20, 3],
    [7, -10, 9],
    [1, -52, 6]
]


rows = len(matrix)
cols = len(matrix[0])
result = [[0]*rows for _ in range(cols)]

for i in range(0,rows):
  for j in range(0,cols):
    result[j][i] = matrix[i][j]
print(result)

for i in range(0,len(result)):
  for j in range(0,len(result[0])):
      print(result[i][j],end=" ")
  print()