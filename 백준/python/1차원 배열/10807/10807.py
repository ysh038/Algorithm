n = int(input())
arr = list(map(int, input().split()))
v = int(input())
result = 0

for i in arr:
    if i == v:
        result+=1
        
print(result)