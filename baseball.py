# key, value = map(int,input().split())
# key_and_value = {}

num = []

print("맞춰야할 숫자 3개를 각각 입력해주세요: ")
for i in range(3):
    num.append(input())

throw = []

cnt = 0
strike = 0
ball = 0

while(strike != 3):
    throw.clear()
    print("숫자 제시! ")
    strike = 0
    ball = 0

    for i in range(3):
        throw.append(input())

    for i in range(len(throw)):
        if throw[i] in num:
            #Stike
            if throw[i] == num[i]:
                strike+=1
            else:
                ball+=1
    cnt += 1

    if strike == 3:
        print(cnt,"번 만에 맞췄습니다.")
    elif strike != 0 or ball != 0:
        print(strike,"Stike",ball,"Ball")  
    else:
        print("OUT!")