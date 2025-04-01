import sys

total_wine = int(sys.stdin.readline())

dp=[0] * total_wine
wine=[] 

for _ in range(total_wine):
    wine.append(int(sys.stdin.readline()))

dp[0] = wine[0]
if total_wine > 1:
    dp[1] = wine[0] + wine[1]
if total_wine > 2:    
    dp[2] = max(wine[0]+wine[2],wine[1]+wine[2],dp[1])

for i in range(3,total_wine):
    dp[i] = max(dp[i-2] + wine[i], dp[i-1], wine[i]+wine[i-1]+dp[i-3])

print(dp[total_wine-1])