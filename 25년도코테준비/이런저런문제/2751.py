import sys

N = int(sys.stdin.readline())
array =[]

for _ in range(N):
    array.append(int(sys.stdin.readline()))

for j in range(N):
    for i in range(N-1): 
        if array[i] > array[i+1]:
            temp = array[i+1]
            array[i+1] = array[i]
            array[i] = temp

for i in range(N):
    print(array[i])