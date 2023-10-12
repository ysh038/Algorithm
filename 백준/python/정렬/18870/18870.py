import sys

N = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))
result = sorted(list(set(array)))

dic = {result[i] : i for i in range(len(result))}

for i in array:
    print(dic[i], end=" ")