import sys
sys.setrecursionlimit(150000)
                      
N, M, R = map(int,sys.stdin.readline().split())
visited = [0] * (N+1)
lines = [[]for _ in range(N+1)]
cnt = 1

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    lines[start].append(end)
    lines[end].append(start)

def dfs(t):
    global cnt
    visited[t] = cnt
    lines[t].sort()
    for line in lines[t]:
        if visited[line] == 0:
            cnt += 1
            dfs(line)

dfs(R)

for i in range(1,N+1):
    print(visited[i])