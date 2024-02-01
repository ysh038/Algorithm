import sys

N, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(array[:K]))

for i in range(N-K):
    result.append(result[i]-array[i]+array[K+i])
print(max(result))