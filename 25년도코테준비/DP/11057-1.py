import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n)]

result = 0

for i in range(10):
    dp[0][i] = 1

for i in range(1,n):
    dp[i][0] = 1
    for j in range(10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for i in range(10):
    result += dp[n-1][i]

print(result%10007)