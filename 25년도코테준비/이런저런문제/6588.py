import sys
import math

prime_num = [True for _ in range(1000001)]
prime_num[0] = prime_num[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(math.sqrt(1000000)) + 1):
    if prime_num[i]:
        j = 2
        while i * j <= 1000000:
            prime_num[i*j] = False
            j += 1

n = int(sys.stdin.readline())

while n != 0:
    if n % 2 != 0:
        print("Goldbach's conjecture is wrong.")
    else:
        found = False
        for k in range(3, n//2 + 1, 2):  # 홀수 소수만 확인 (2 제외)
            if prime_num[k] and prime_num[n-k]:
                print(f"{n} = {k} + {n-k}")
                found = True
                break
        
        if not found:
            print("Goldbach's conjecture is wrong.")
            
    n = int(sys.stdin.readline())
