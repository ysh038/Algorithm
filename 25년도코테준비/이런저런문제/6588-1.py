import sys
import math

prime = [True for _ in range(1000001)]

prime[0], prime[1] = False, False

for i in range(2,int(math.sqrt(10000001))+1):
    j=2
    if prime[i] == True:
        while(i*j < 1000001):
            prime[i*j] = False
            j+=1

n = int(sys.stdin.readline())

while(n != 0):
    if n % 2 != 0:
        print("Goldbach's conjecture is wrong.")

    found = False
    for k in range(3, n//2 + 1, 2):  # 홀수 소수만 확인 (2 제외)
        if prime[k] and prime[n-k]:
            print(f"{n} = {k} + {n-k}")
            found = True
            break
    
    if not found:
        print("Goldbach's conjecture is wrong.")
            
    n = int(sys.stdin.readline())