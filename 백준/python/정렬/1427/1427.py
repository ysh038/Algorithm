import sys

array = list(map(int,input()))

for i in range(len(array)):
    for j in range(1,len(array)):
        if array[i] < array[j] and i < j:
            array[i], array[j] = array[j], array[i]

for i in array:
    print(i,end="")