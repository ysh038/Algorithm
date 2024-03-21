import sys

K, N = map(int,sys.stdin.readline().split())
line_list = []

for _ in range(K):
    line_list.append(int(sys.stdin.readline()))

line_list.sort()

left = 1
right = max(line_list)

while left <= right:
    temp = 0
    mid = (left + right) // 2

    for line in line_list:
        temp += (line // mid)
        
    if temp < N:
        right = mid - 1
    else:
        left = mid + 1
print(right)