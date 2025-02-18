import sys

word = list(sys.stdin.readline().strip())
index = 0

for i in word:
    print(i,end="")
    index += 1
    if(index == 10):
        print('')
        index = 0