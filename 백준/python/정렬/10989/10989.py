import sys

N = int(sys.stdin.readline())

array = [0] * N

for i in range(N):
    array[i] = int(sys.stdin.readline())

print(len(array))

array.sort()

for i in array:
    print(i)