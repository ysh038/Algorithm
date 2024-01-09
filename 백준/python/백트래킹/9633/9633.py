import sys

N = int(sys.stdin.readline())

cnt = 0
queen_visited = [[False] * (N)] * (N)

def dfs():
    global cnt
    for w in range(N):
        for h in range(N):
            queen_visited[w][h] = True        
    
    return cnt

print(dfs())