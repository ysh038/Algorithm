import sys

board = [list(map(int,sys.stdin.readline().split()))for _ in range(9)]
zero = []
num = 0
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])

def column(x):
    for i in range(9):
        if num == board[i][x]:
            return False
    return True

def row(y):
    for i in range(9):
        if num == board[y][i]:
            return False
    return True

def square(x, y):
    for i in range(3):
        for j in range(3):
            if num == board[y // 3 * 3 + i][x // 3 * 3 + j]:
                return False
    return True

def dfs(cnt):
    global num
    if cnt == len(zero):
        for i in range(9):
            print(*board[i])
        exit()

    for i in range(1,10):
        y = zero[cnt][0]
        x = zero[cnt][1]
        num = i
        if column(x) and row(y) and square(x,y):
            board[y][x] = i
            dfs(cnt+1)
            board[y][x] = 0
            
dfs(0)