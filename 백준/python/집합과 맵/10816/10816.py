import sys

N = int(sys.stdin.readline())
sangguen_card_array = []
sangguen_card_array = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
compare_card_array = []
compare_card_array = list(map(int,sys.stdin.readline().split()))

compare_card_set = {}

for i in compare_card_array:
    compare_card_set[i] = 0

for i in sangguen_card_array:
    if i in compare_card_set:
        compare_card_set[i] += 1

for i in compare_card_array:
    if i in compare_card_set:
        print(compare_card_set[i], end=" ")
    else:
        print(0, end=" ")
