N,M=map(int,input().split())

array= [0] * (N)

for i in range(M):
    i,j,k = map(int,input().split())
    for index in range(i-1,j):
        array[index] = k

for i in array:
    print(i,end=" ")