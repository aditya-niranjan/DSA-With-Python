
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

rows = len(board)
cols = len(board[0])

def rowsCheck(board):

    for i in range(rows):
        sudko = set()
        for j in range(cols):
            if board[i][j] == ".":
                continue
            if board[i][j] in sudko:
                return False
            sudko.add(board[i][j])
    
    return True

def colsCheck(board):
    for i in range(cols):
        sudko = set()
        for j in range(rows):
            if board[j][i] == ".":
                continue
            if board[j][i] in sudko :
                return False
            sudko.add(board[j][i])
    
    return True
print(rowsCheck(board))
print(colsCheck(board))

def boxCheck(board):
    for i in range(3):
        for j in range(3):
            sudko = set()
            for k in range(3):
                for l in range(3):
                    if board[i*3+k][j*3+l] == ".":
                        continue
                    if board[i*3+k][j*3+l] in sudko:
                        return False
                    sudko.add(board[i*3+k][j*3+l])
    
    return True

print(boxCheck(board))