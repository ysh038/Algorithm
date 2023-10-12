import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    array.append(sys.stdin.readline().strip())

array = list(set(array))

array.sort()

array = sorted(array,key = lambda x : len(x))

for i in array:
    print(i)