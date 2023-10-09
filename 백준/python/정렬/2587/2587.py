array = []
sum, avg = 0, 0
for i in range(5):
    array.append(int(input()))

for i in array:
    sum += i
avg = sum // 5

array.sort()
print(avg)
print(array[2])