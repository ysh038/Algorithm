import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_result = - int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, sum,idx):
    global result
    global max_result
    global min_result

    if idx == N:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return 
    
    if add:
        dfs(add-1, sub, mul, div, sum+array[idx],idx+1)

    if sub:
        dfs(add, sub-1, mul, div, sum-array[idx],idx+1)

    if mul > 0:
        dfs(add, sub, mul-1, div,sum*array[idx],idx+1)

    if div > 0:
        dfs(add, sub, mul, div-1, int(sum/array[idx]),idx+1)

dfs(add, sub, mul, div, array[0],1)

print(max_result)
print(min_result)