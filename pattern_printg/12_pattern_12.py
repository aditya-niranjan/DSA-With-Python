
n = int(input("Enter the value: "))

# for i in range(n):
#     if i < n // 2:
#         print(" " * (i), end="")
#         print("* " * (n//2-i),end="")
#     else:
#         print(" " * (n-i-1),end="")
#         print("* " * (i+1 - (n//2)),end="")
#     print()

  # total rows for each half

# 🔹 Part 1: Inverted Pyramid
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# 🔹 Part 2: Normal Pyramid
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


