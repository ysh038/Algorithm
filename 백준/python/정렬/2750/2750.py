N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
for i in range(N):
    for j in range(i+1,N):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

for i in array:
    print(i)