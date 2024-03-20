import sys

_ = int(sys.stdin.readline())
card_list = sorted(map(int,sys.stdin.readline().split()))

_ = int(sys.stdin.readline())
answer_list = map(int,sys.stdin.readline().split())

def binary(n, card_list, left, right):
    if left > right:
        return 0
    mid = (left + right) // 2

    if n == card_list[mid]:
        return card_list[left:right+1].count(n)
    elif n < card_list[mid]:
        return binary(n, card_list, left, mid - 1)
    else:
        return binary(n, card_list, mid+1, right)
    
N_dict = {}

for n in card_list:
    left = 0
    right = len(card_list) - 1
    if n not in N_dict:
        N_dict[n] = binary(n, card_list, left, right)

for m in answer_list:
    if m in N_dict:
        print(N_dict[m],end=" ")
    else:
        print(0,end=" ")
        
# print(' '.join(str(N_dict[x]) if x in N_dict else '0' for x in answer_list ))