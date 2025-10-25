
#bruth force approcah so make sure to check the otimal solution for this 


prices  = [7,2,1,5,6,3,4,8]

n = len(prices)
max_profit = 0

for i in range(0,n):
  for j in range(i+1,n):
      recent_profit = (prices[j] - prices[i])
      max_profit = max(recent_profit,max_profit)
print(max_profit)