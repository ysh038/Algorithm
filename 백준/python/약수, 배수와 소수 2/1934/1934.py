import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    i, j = map(int,sys.stdin.readline().split())
    gcd = math.gcd(i,j)
    print(int((i*j)/gcd))