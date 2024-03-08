import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

A.sort()

for i in range(M):
    A_index = N//2
    if num_list[i] < A[A_index]:
        A_index //= 2
    elif num_list[i] > A[A_index]:
        A_index *= 2
    elif num_list[i] == A[A_index]:
        print(1)
    else:

def binarySearch(index):
    if num_list[index] < A[N//2]:
        index = 
    elif num_list[i] > A[M//2]: