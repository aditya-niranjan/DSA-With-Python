
from turtle import end_fill


matrix = [
  [7,9,2,3],
  [20,8,0,10],
  [29,0,-10,5],
  [4,14,6,7]
]

rows = len(matrix)
cols = len(matrix[0])

rowstrack = [0 for _ in range(rows)]
colstrack = [0 for _ in range(cols)]

for i in range(0,rows):
  for j in range(0,cols):
    if matrix[i][j] == 0:
      rowstrack[i]=float("inf")
      colstrack[j]=float("inf")

for i in range(0,rows):
  for j in range(0,cols):
    if rowstrack[i] == float("inf") or colstrack[j]== float("inf"):
        matrix[i][j]=0


for i in range(0,rows):
  for j in range(0,cols):
    print(matrix[i][j],end="  ")
  print()
