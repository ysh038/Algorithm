array =[]
for i in range(9):
    a = int(input())
    array.append(a)
max = array[0]

for i in array[1:]:
    if i > max:
        max = i

# print(max,"\n",(array.index(max)+1))
print(max)
print((array.index(max)+1))