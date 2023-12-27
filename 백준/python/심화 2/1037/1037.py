import sys

factors = []
num_factors = int(sys.stdin.readline())

factors = list(map(int,sys.stdin.readline().split()))
factors.sort()

print(factors[0] * factors[num_factors-1])