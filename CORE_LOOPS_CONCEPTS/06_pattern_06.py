
n = int(input("Enter a number: "))
def concentric_square_pattern(n):
    size = 2 * n - 1  # total rows and columns

    for row in range(size):
        for col in range(size):
            # Calculate the minimum distance from any edge
            min_dist = min(row, col, size - 1 - row, size - 1 - col)
            print(n - min_dist, end="  ")
        print()

# Run it for n = 4
concentric_square_pattern(n)
