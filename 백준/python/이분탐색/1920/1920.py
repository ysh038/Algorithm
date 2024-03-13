import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

A.sort()

for num in num_list:
    isExist = False
    left = 0
    right = N - 1

    while left <= right:
        middle = (left + right) // 2
        if num < A[middle]:
            right = middle - 1
        elif num > A[middle]:
            left = middle + 1
        else:
            isExist = True
            print(1)
            break
    if not isExist:
        print(0)
