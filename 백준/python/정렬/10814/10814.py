import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(list(sys.stdin.readline().split()))
    array[i][0] = int(array[i][0])

array = sorted(array, key=lambda x : x[0])

for i in array:
    print(i[0],i[1])