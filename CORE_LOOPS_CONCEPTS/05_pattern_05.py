n = int(input("Enter a number: "))
for i in range(2 * n):
        totalcol = 2 * n - i if i > n else i
        totalspace = n - totalcol
        print(" " * totalspace, end="")
        for j in range(totalcol):
            print("* ", end="")
        print()
