import sys

N = int(sys.stdin.readline())

def facto(num):
    if num > 0:
        return num * facto(num - 1)
    else:
        return 1

print(facto(N))