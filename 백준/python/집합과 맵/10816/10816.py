import sys

N = int(sys.stdin.readline())

sangguen_card = {}

for i in range(N):
    sangguen_card[i] = int(sys.stdin.readline())

M = int(sys.stdin.readline())

compare_card_set = {}

for i in range(M):
    compare_card_set[int(sys.stdin.readline())] = i

# for i in sangguen_card:
#     if i in compare_card_set:
#         print("shit")

print(compare_card_set)