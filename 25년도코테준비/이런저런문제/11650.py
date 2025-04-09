import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    array.append(list(map(int,sys.stdin.readline().split())))

def merge(left_array, right_array):
    left_index, right_index = 0,0
    new_array = []

    while left_index < len(left_array) and right_index < len(right_array):
        if(left_array[left_index][0] > right_array[right_index][0]):
            new_array.append(right_array[right_index])
            right_index+=1
        elif(left_array[left_index][0] == right_array[right_index][0]):
            if(left_array[left_index][1] > right_array[right_index][1]):
                new_array.append(right_array[right_index])
                right_index+=1
            else:
                new_array.append(left_array[left_index])
                left_index += 1
        else:
            new_array.append(left_array[left_index])
            left_index+=1

    while left_index < len(left_array):
        new_array.append(left_array[left_index])
        left_index+=1
    while right_index < len(right_array):
        new_array.append(right_array[right_index])
        right_index+=1

    return new_array

def sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2

    left_array = sort(array[:mid])
    right_array = sort(array[mid:])

    return merge(left_array,right_array)


sorted_array = sort(array)
for i in range(N):
    print(sorted_array[i][0],sorted_array[i][1])
