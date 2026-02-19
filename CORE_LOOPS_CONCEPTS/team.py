n = int(input())  # Number of problems
count = 0         # To count how many problems they'll solve

for _ in range(n):
    opinions = list(map(int, input().split()))  # Read 3 values for each problem
    if sum(opinions) >= 2:  # If at least two friends are sure
        count += 1

print(count)  # Output the number of problems they will solve

