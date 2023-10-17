N, M = map(int,input().split())
S =  set({})
cnt_result = 0

for i in range(N):
    S.add(input())

for i in range(M):
    temp = input()
    if temp in S:
        cnt_result+=1

print(cnt_result)