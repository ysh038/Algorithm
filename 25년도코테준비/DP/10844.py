import sys

N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N)]

for i in range(1,10):
    dp[0][i] = 1

result = 0
for i in range(1,N):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

for i in range(10):
    result+=dp[N-1][i]
print(result % 1000000000)