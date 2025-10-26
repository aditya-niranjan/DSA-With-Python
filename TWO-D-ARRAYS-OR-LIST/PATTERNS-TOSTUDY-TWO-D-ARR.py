


def UpperTriangle(nums):

  
  rows = len(nums)
  cols = len(nums[0])

  for i in range(0,rows):
    for j in range(0,cols):
      if j>=i:
          print(nums[i][j],end="  ")
      else:
          print("*",end=" ")
    print()


def LowerTriangle(nums):
   
  rows = len(nums)
  cols = len(nums[0])

  for i in range(0,rows):
    for j in range(0,cols):
      if i>=j:
          print(nums[i][j],end="  ")
      else:
          print("*",end=" ")
    print()

def Diagonal(nums):
   
  rows = len(nums)
  cols = len(nums[0])

  for i in range(0,rows):
    for j in range(0,cols):
      if i==j:
          print(nums[i][j],end="  ")
      else:
          print("*",end=" ")
    print()

def Right_Diagonal(nums):
   
  rows = len(nums)
  cols = len(nums[0])

  for i in range(0,rows):
    for j in range(0,cols):
      if i + j == rows - 1 : 
          print(nums[i][j],end="  ")
      else:
          print("*",end=" ")
    print()

nums = [
    [5, 20, 3],
    [7,10, 9],
    [1,52,6]
]

UpperTriangle(nums)
print()
LowerTriangle(nums)
print()
Diagonal(nums)
print()
Right_Diagonal(nums)