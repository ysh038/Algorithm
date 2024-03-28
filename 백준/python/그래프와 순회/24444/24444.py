import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N,M,R = map(int,sys.stdin.readline().split())
lines = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 1

for _ in range(M):
    start,end = map(int,sys.stdin.readline().split())
    lines[start].append(end)
    lines[end].append(start)

for i in range(N+1):
    lines[i].sort()

def bfs(start):
    global cnt
    visited[start] = cnt
    queue = deque([start])
    while queue:
        index = queue.popleft()
        for i in lines[index]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt

bfs(R)
for i in range(1,N+1):
    print(visited[i])
