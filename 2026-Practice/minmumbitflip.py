start = 3
goal = 4

ans = start ^ goal
count = 0
for i in range(32):
  if ans & (1<<i)!=0:
    count+=1
  
print(count)