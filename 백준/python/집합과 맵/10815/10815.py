import sys

N = int(sys.stdin.readline())
array = list(map(int,(sys.stdin.readline().split())))

M = int(sys.stdin.readline())
compared_array = list(map(int,(sys.stdin.readline().split())))

compared_dictionary = {}

for i in compared_array:
    compared_dictionary[i] = 0

for i in array:
    if i in compared_dictionary:
        compared_dictionary[i] = 1

for i in compared_dictionary:
    print(compared_dictionary[i], end=" ")