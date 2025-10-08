

from ast import Num


def counting(n):
    num = n
    count = 0

    while num > 0:
        count+=1
        num = num //10
    return count


n = 5438

result = counting(n)

print(f"the number of digits: {result}")



