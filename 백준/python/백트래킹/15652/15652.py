import sys

N, M = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
    else:
        for i in range(1, N+1):
            if len(s)!= 0 and s[len(s)-1] > i:
                continue
            else:
                s.append(i)
                dfs()
                s.pop()
dfs()