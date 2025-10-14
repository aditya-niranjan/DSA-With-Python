

n = 50
prime_numebers = []
not_prime_numbers = []
if n <=1:
  print("number is not a prime number")
else:
  for i in range(2,n+1):
    if n % i == 0:
      print(f"not prime numbers {i}")
      not_prime_numbers.append(i)
    else:
      print(f"the number is prime -- {i} ")
      prime_numebers.append(i) 


print(f"total prime unders {n} is {len(prime_numebers)}")
print(f"total non prime numbers unders {n} is {len(not_prime_numbers)}")
