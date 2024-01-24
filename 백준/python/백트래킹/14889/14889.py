import sys

N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
visited = [False for _ in range(N)]

min = int(1e9)

def dfs(i,j):
    global min

    if i == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    s1 += S[i][j]
                elif not visited[i] and not visited[j]:
                    s2 += S[i][j]
        min = min(min, abs(s1-s2))

dfs(0,0)
print(min)