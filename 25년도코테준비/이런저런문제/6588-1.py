import sys
import math

prime = [True] * 1000001
prime[0] = False
prime[1] = False

for i in range(2,int(math.sqrt(1000000))+1):
    if prime[i] == True:
        j = 2
        while(i*j) < 1000001:
            prime[i*j] = False
            j+=1
        
print(prime[3],prime[10],prime[17])
