

# import re
# from turtle import distance
# from unittest import result

# from pyparsing import col


# grid = [[1,0,0],[0,0,0],[0,0,1]]



# result = []


# def findThief(grid):
#       rows = len(grid)
#       cols = len(grid[0])

#       for row in range(rows):
#            for col in range(cols):
#                 if grid[row][col] == 1:
#                     result.append((row, col))

#       return result

# def manhattan_distance(result):
      
#       total = len(result)

#       for i in range(total):
#             for j in range(i + 1, total):
#                   distance = abs(result[i][0] - result[j][0]) + abs(result[i][1] - result[j][1])
#                   print(f"Distance between {result[i]} and {result[j]}: {distance}")
       


# # print(result)

# print(findThief(grid))
# manhattan_distance(findThief(grid))


grid = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]


def find_thieves(grid):
    thieves = []

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                thieves.append((r, c))

    return thieves


def nearest_thief_distance(grid, thieves):
    rows = len(grid)
    cols = len(grid[0])

    distance_matrix = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):

            minimum = float("inf")

            for tr, tc in thieves:
                distance = abs(r - tr) + abs(c - tc)
                minimum = min(minimum, distance)

            distance_matrix[r][c] = minimum

    return distance_matrix


thieves = find_thieves(grid)

print("Thieves:", thieves)

matrix = nearest_thief_distance(grid, thieves)

print("\nDistance Matrix:")
for row in matrix:
    print(row)


# we need to find the safest path from the top-left corner (0, 0) to the bottom-right corner (rows-1, cols-1) of the grid. The safest path is defined as the path that maximizes the minimum distance to any thief along the path.

