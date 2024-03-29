import sys

N,M = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
prefix_sum = [0]

temp = 0

for i in array:
    temp += i
    prefix_sum.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])