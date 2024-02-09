import sys

n = int(sys.stdin.readline())
array = [0]
dp = [0] * (n+1)

for _ in range(n):
    array.append(int(sys.stdin.readline()))

dp[1] = array[1]

if n >= 2:
    dp[2] = array[1] + array[2]

if n >= 3:
    dp[3] = max(array[1]+array[3],array[2]+array[3],dp[2])

for i in range(4,n+1):
    dp[i] = max(dp[i-1],dp[i-3] +array[i-1] + array[i], dp[i-2] + array[i])

print(dp[n])