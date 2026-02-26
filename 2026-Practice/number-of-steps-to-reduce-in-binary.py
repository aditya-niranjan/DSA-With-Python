
# binary_number = "1110"
# decimal_number = int(binary_number, 2)

# steps = 0

# # if decimal_number == 2:
# #     steps+=1
# #     print(steps)
# #     exit()
# # if decimal_number == 1:
# #     print(steps)
# #     exit()

# while decimal_number > 0:

#     if decimal_number % 2 == 0:
#         decimal_number //= 2
#     else:
#         decimal_number += 1
#     steps += 1

# print(steps)

binary_number = "1110"

steps = 0
carry = 0

# Traverse from right to left (ignore first bit)
for i in range(len(binary_number) - 1, 0, -1):
    bit = int(binary_number[i]) + carry
    
    if bit == 1:
        # odd → add 1 → becomes even
        steps += 2
        carry = 1
    else:
        # even → divide by 2
        steps += 1

# If carry remains, one extra step needed
print(steps + carry)