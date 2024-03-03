import sys

N = int(sys.stdin.readline())
time_list = []
cnt = 0

for _ in range(N):
    start, end = map(int,sys.stdin.readline().split())
    time_list.append([start, end])

time_list.sort(key=lambda x : (x[1], x[0]))

cnt = 1
end_time = time_list[0][1]

for i in range(1,N):
    if time_list[i][0] >= end_time:
        cnt += 1
        end_time = time_list[i][1]
    else:
        continue
print(cnt)