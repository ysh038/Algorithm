word = input()
count = [0] * (ord('z')-ord('a')+1)
max = max_index = 0
isRedundant = False

# 편리한 비교를 위해 모두 대문자로 변환
word = word.upper()

for i in word:
    count[ord(i)-ord('A')] += 1

for i in range(len(count)):
    if(count[max_index] < count[i]):
        isRedundant = False
        max_index = i
    elif(count[max_index] == count[i]):
        if(i != 0):
            isRedundant = True

if(isRedundant):
    print("?")
else:
    print(chr(max_index+ord('A')))
