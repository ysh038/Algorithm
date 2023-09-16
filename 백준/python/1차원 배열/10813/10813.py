# N, M = map(int,input().split())

# array = [0] * N

# for i in range(N):
#     array[i] = i+1

# for i in range(M):
#     index1, index2 = map(int, input().split())
#     temp = array[index1-1]
#     array[index1-1] = array[index2-1]
#     array[index2-1] = temp

# for i in array:
#     print(i,end=" ")
N, M = map(int,input().split())

array = [0] * N

for i in range(N):
    array[i] = i+1

for i in range(M):
    index1, index2 = map(int, input().split())
    array[index1-1], array[index2-1] = array[index2-1], array[index1-1]

for i in array:
    print(i,end=" ")