
matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
       print(matrix[i][j],end="  ")
    print()

print()
n = len(matrix)

for i in range(0,n-1):
  for j in range(i+1,n):
    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in range(0,n):
  matrix[i].reverse()

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
       print(matrix[i][j],end="  ")
    print()

