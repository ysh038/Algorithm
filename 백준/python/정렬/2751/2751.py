import sys

N = int(sys.stdin.readline())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))
array.sort()

for i in array:
    print(i)