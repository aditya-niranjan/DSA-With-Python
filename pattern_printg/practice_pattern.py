
for i in range(8):
    for j in range(10):
        if i == 0 or i ==7:
            print("*", end="")
        elif i == 1 or i == 6:
            if j< 3 or j>6:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 2 or i == 5:
            if j < 2 or j > 7:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 3 or i == 4:
            if j == 0 or j == 9:
                print("*", end="")
            else:
                print(" ", end="")  
    print()  # move to next line  