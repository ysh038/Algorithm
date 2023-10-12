import sys

N, k = map(int, sys.stdin.readline().split())

students = list(map(int, sys.stdin.readline().split()))

students = sorted(students,reverse=True)

print(students[k-1])