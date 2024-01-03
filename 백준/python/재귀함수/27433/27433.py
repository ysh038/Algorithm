import sys

N = int(sys.stdin.readline())

def factorial(num):
    if num > 0:
        return num * factorial(num-1)
    else:
        return 1

print(factorial(N))