N,M = map(int, input().split())

array = []

for i in range(N):
    array.append(i+1)

for i in range(M):
    i,j = map(int, input().split())
    # python 식 swap 문법
    array[i-1], array[j-1] = array[j-1], array[i-1]

for i in array:
    print(i,end=" ")