import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
cnt = 0

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for coin in coins[::-1]:
    if K == 0:
        break
    if K >= coin:
        cnt = cnt + (K // coin)
        K %= coin

print(cnt)