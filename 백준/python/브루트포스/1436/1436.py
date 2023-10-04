N = int(input())
cnt = 0
index = 0

while(1):
    if '666' in str(index):
        cnt += 1
    if cnt == N:
        print(str(index))
        exit(0)
    index+=1