import sys

N = int(sys.stdin.readline())
array =[]

for _ in range(N):
    array.append(int(sys.stdin.readline()))

def merge(left_array, right_array):
    new_array = []
    left_index,right_index = 0,0
    
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] > right_array[right_index]:
            new_array.append(right_array[right_index])
            right_index+=1
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
    
    middle = len(array) // 2
    
    left_array = sort(array[:middle])
    right_array = sort(array[middle:])
    
    return merge(left_array, right_array)
    
sorted_array = sort(array)

for i in range(len(array)):
    print(sorted_array[i])