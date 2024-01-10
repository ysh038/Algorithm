import sys

N = int(sys.stdin.readline())

cnt = 0
queen_visited = [[False] * (N)] * (N)

def dfs():
    global cnt
    for w in range(N):
        for h in range(N):
            if queen_visited[w][h] != False:
                queen_visited[w][h] = True
                cnt += 1
                dfs()
                queen_visited[w][h] = False
            else:
                continue
    
    return cnt

print(dfs())