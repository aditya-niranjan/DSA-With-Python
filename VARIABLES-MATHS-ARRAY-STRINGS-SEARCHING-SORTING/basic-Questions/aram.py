
def aramusingNoraml(n):
    temp = n
    num_count = 0

    for num in temp:
        temp = temp // 10
        num_count += 1

    temp = n
    divisor = 10 ** (num_count - 1)
    total = 0

    for _ in (num_count):
        digit = temp // divisor
        total+= digit ** (num_count)
        temp = temp % divisor
        divisor = divisor // 10
    return total

n = 153
result = aramusingNoraml(n)

print("ArmStrongNumber " if n == result else "NOT --- ArmStrongNumber")
  
