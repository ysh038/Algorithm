N, M = map(int,input().split())
card = list(map(int,input().split()))

max_result = 0

for i in range(N-1, -1,-1):
    for j in range(i-1,-1,-1):
        for k in range(j-1,-1,-1):
            if card[i]+card[j]+card[k] > max_result and card[i]+card[j]+card[k] <= M :
                max_result = card[i]+card[j]+card[k]

print(max_result)