import sys

n = int(sys.stdin.readline())

def fibonacci(num):
    if num > 1:
        return (fibonacci(num-1) + fibonacci(num-2))
    else:
        return num

print(fibonacci(n))