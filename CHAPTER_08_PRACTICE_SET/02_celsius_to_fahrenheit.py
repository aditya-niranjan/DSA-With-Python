




import re


a = int(input("Enter temperature in Celsius: "))

def c_to_f(a):
  return round((5 *(a - 32)/9),3)

result = c_to_f(a)

print(f"{result}°C")
