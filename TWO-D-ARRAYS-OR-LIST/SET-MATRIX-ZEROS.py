
class SetZerosMatrix:
    
    def Set_Zeros(self,matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    self.Mark_infinity(matrix,i,j)

        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                  if matrix[i][j] == float("inf"):
                      matrix[i][j]=0
        return self.Display_result(matrix)
    
    def Mark_infinity(self,matrix,rows,cols):
      
        r =len(matrix)
        c = len(matrix[0])

        for i in range(0,r):
            if matrix[i][cols] != 0:
                matrix[i][cols]=float("inf")

        for j in range(0,c):
            if matrix[rows][j] !=0:
                matrix[rows][j]=float("inf")
    def Display_result(self,matrix):
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                print(matrix[i][j],end=" ")
            print()
        

matrix = [
  [7,9,2,3],
  [20,8,0,10],
  [29,0,-10,5],
  [4,14,6,7]
]

s1 = SetZerosMatrix()
s1.Set_Zeros(matrix)
