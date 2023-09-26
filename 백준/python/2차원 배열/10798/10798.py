array = []

for i in range(5):
    word = list(input())
    array.append(word)

result_array = []
result_array = [[0 for i in range(5)]for j in range(15)]

for i in range(len(array)):
    for j in range(len(array[i])):
        result_array[j][i] = array[i][j]

for i in result_array:
    for j in i:
        if j != 0:
            print(j,end="")