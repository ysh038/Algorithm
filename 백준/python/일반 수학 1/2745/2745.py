number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()
B = int(B)

result = 0

for i in range(len(N)):
    result += number.find(N[i]) * B**(len(N)-(i+1))

print(result)