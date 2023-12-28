import sys

N, M = map(int, sys.stdin.readline().split())
word_array = []

for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    else:
        word_array.append(word)

set(word_array)