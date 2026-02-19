for i in range(8):  # total 8 rows
    for j in range(10):  # total 10 columns
        if i == 0 or i == 7:  # first and last row full
            print("*", end="")
        elif i == 1 or i == 6:  # second and second-last
            if j < 3 or j > 6:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 2 or i == 5:  # third and third-last
            if j < 2 or j > 7:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 3 or i == 4:  # middle two rows
            if j == 0 or j == 9:
                print("*", end="")
            else:
                print(" ", end="")
    print()  # move to next line
