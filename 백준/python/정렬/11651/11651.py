import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

array = sorted(array,key=lambda x : (x[1],x[0]))

for i in array :
    print(i[0],i[1])