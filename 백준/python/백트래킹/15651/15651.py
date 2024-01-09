import sys

N,M = map(int, sys.stdin.readline().split())

s = []
# visited = [False] * (N+1)

def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
    else:
        for i in range(1,N+1):
            s.append(i)
            dfs()
            s.pop()

dfs()