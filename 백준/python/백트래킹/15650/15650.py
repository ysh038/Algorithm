import sys

N, M = map(int, sys.stdin.readline().split())

s = []
visited = [False] * (N+1)

def DFS():
    if len(s) == M:
        print(' '.join(map(str,s)))
    else:
        for i in range(1,N+1):
            if visited[i] == False:
                if len(s) == 0:
                    s.append(i)
                    visited[i] == True
                    DFS()
                    s.pop()
                    visited[i] == False
                elif s[len(s)-1] < i:
                    s.append(i)
                    visited[i] == True
                    DFS()
                    s.pop()
                    visited[i] == False
                else:
                    continue

DFS()