N = int(input())
result = 0

for i in range(N//5,-1,-1):
    remain = N-(5*i)
    if(remain % 3 == 0):
        result = i + (remain//3)
        print(result)
        exit(0)
print(-1)