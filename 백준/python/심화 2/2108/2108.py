import sys
import math

array = []
N = int(sys.stdin.readline())

for i in range(N):
    array.append(float(sys.stdin.readline()))

N_sum = 0
N_sorted = sorted(array)
N_sorted_reverse = sorted(array,reverse=True)
N_dict = {}
N_set = set(array)
N_largest = N_sorted_reverse[0]
N_second_larges = N_sorted_reverse[0]

for i in N_sorted_reverse:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

for i in N_dict:
    if N_dict[N_largest] <= N_dict[i]:
        N_second_larges = N_largest
        N_largest = i

for i in array:
    N_sum += i

print(round(N_sum/N))
print(round(N_sorted[math.trunc(N/2)]))
if N_dict[N_largest] == N_dict[N_second_larges]:
    print(round(N_second_larges))
else:
    print(round(N_largest))
print(round(N_sorted[len(N_sorted)-1] - N_sorted[0]))