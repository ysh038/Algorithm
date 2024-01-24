import sys

N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
visited = [False for _ in range(N)]

m_min = int(1e9)

def dfs(i,j):
    global m_min

    if i == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    s1 += S[i][j]
                elif not visited[i] and not visited[j]:
                    s2 += S[i][j]
        m_min = min(m_min, abs(s1-s2))
        return

    for k in range(j, N):
        if not visited[k]:
            visited[k] = True
            dfs(i+1, k+1)
            visited[k] = False

dfs(0,0)
print(m_min)