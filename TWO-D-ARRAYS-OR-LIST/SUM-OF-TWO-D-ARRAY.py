
# this how we use to itearte the two-2 list or array you can say 


two_d_arr = [
    [5, 20, 3],
    [7, -10, 9],
    [1, -52,6]
]

total_sum_of_all_elemnts = 0

rows = len(two_d_arr)
cols = len(two_d_arr[0])

for i in range(0,rows):
  for j in range(0,cols):
    total_sum_of_all_elemnts+=two_d_arr[i][j]

print(total_sum_of_all_elemnts)