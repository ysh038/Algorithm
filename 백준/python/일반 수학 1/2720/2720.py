T = int(input())

for i in range(T):
    C = int(input())
    print(C // 25,end=" ")
    C %= 25
    print(C // 10,end=" ")
    C %= 10
    print(C // 5,end=" ")
    C %= 5
    print(C // 1,end=" ")
    C %= 1