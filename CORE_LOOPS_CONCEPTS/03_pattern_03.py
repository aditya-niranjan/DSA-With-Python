
# this code  is only run for the patterns which have the  number of rows of  odd 

#this below return code it depend on the my logic 

n = int(input("Enter a number: "))
for i in range(2 * n):
        totalcol = 2 * n - i if i > n else i
        for j in range(totalcol):
            print("* ", end="")
        print()


# this below code is kunal kushwa's code logic that i transalated into the python code

# n = int(input("Enter a number: "))


# def pattern5(n):
#     for row in range(2 * n):
#         totalColsInRow = 2 * n - row if row > n else row
#         for col in range(totalColsInRow):
#             print("* ", end="")
#         print()

# # Example
# pattern5(n)
