# Write a Python program to check whether a given number is an Armstrong number or not.

# An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.

# For example:

# 153 is an Armstrong number because
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 


def ArmStrongNumber(n):
  num = n
  node = len(str(n))
  total = 0

  while num > 0:
    lastdigit = num % 10
    total = total + (lastdigit ** node)
    num = num // 10
  return total


n = 16

result = ArmStrongNumber(n)

print("ArmStrongNumber " if n == result else "NOT --- ArmStrongNumber")
  
