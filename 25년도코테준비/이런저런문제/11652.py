import sys

N = int(sys.stdin.readline())
card = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

max_value = max(card.values())

max_keys = []
for key,value in card.items():
    if value == max_value:
        max_keys.append(key)

print(min(max_keys))