import sys

T = int(sys.stdin.readline())

def recursion(word,left,right,cnt):
    cnt += 1
    if left >= right:
        return 1, cnt
    elif word[left] != word[right]:
        return 0, cnt
    else:
        return recursion(word, left+1, right-1, cnt)

for i in range(T):
    word = input()
    is_palindrom, cnt = recursion(word,0,len(word)-1,0)
    print(is_palindrom, cnt)