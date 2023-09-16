N = int(input())

# score = []

# array = input().split()

# for i in array:
#     score.append(int(i))

score = list(map(int, input().split()))

max = score[0]

for i in score[1:]:
    if i > max:
        max = i

for i in range(N):
    score[i] = score[i]/max*100

sum = 0

for i in score:
    sum += i

average = sum/N

print(average)