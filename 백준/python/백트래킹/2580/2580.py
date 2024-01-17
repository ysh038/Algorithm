import sys

board = [list(map(int,sys.stdin.readline().split()))for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])

def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            print(*board[i])
        exit()
    x = zero[cnt][0]


dfs(0)