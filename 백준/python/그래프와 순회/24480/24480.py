import sys
sys.setrecursionlimit(150000)

N, M, R = map(int,sys.stdin.readline().split())
lines = [[] for _ in range(N+1)]
cnt = 1
visited = [0] * (N+1)

for i in range(1,M+1):
    start, end = map(int, sys.stdin.readline().split())
    lines[start].append(end)
    lines[end].append(start)


def dfs(start):
    global cnt
    visited[start] = cnt
    lines[start].sort(reverse=True)
    cnt += 1
    for end in lines[start]:
        if visited[end] == 0:
            dfs(end)
        
dfs(R)
for i in range(1,N+1):
    print(visited[i])