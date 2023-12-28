import sys

N, M = map(int, sys.stdin.readline().split())
word_array = []

for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    else:
        word_array.append(word)

word_array.sort(key=lambda x : (-len(x),x))

word_dict = {}
for word in word_array:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
sorted_with_frequency = sorted(word_dict.items(),key=lambda x: x[1], reverse=True)

sorted_with_frequency_list = []
for word in sorted_with_frequency:
    sorted_with_frequency_list.append(word[0]) # 빈도 수를 기준으로 정렬한 key, value 쌍의 list 의 key값으로 다시 list만들기

for word in sorted_with_frequency_list:
    print(word)