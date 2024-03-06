import sys

A, B, C = map(int, sys.stdin.readline().split())

def conquer(a,b,c):
    if b == 1:
        return a % c
    elif b % 2 == 1: # 홀수
        return conquer(a,b//2,c) ** 2 * a % c
    else: # 짝수
        return conquer(a,b//2,c) ** 2 % c

result = conquer(A,B,C)
print(result)