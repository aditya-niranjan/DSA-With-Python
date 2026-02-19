

from itertools import count
from pickle import TRUE


counttotal = 0

for num in range(2,51):
  is_prime = TRUE
  counttotal+=1
  if num == 1 or num == 0:
    print("not prime number")
  else:
    for i in range(2,num):
      if num % i == 0:
        is_prime = False
        break

  if is_prime:
    print(f"{num} is prime number")

    print(sum[counttotal])