max_value = column = row = 0
array = []

for i in range(9):
    a = list(map(int,input().split()))
    array.append(a)
    if max_value < max(a):
        max_value = max(a)
        column = a.index(max_value)+1
        row = i+1

if(max_value == 0 and row == 0 and column == 0):
    print(max_value)
    print(1,1)
else:
    print(max_value)
    print(row, column)