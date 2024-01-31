import sys

N = int(sys.stdin.readline())
array = []
dp = [0] * (N)

for i in range(N):
    array.append(int(sys.stdin.readline()))

dp[0] = array[0]
dp[1] = array[1] + dp[0]
dp[2] = max(array[0]+array[1],array[1]+array[2])

for i in range(3,N):
    dp[i] = max(dp[i-3] + array[i-1] + array[i],dp[i-2] + array[i])

print(dp[N-1])