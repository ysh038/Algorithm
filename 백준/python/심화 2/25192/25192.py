import sys

chat_num = int(sys.stdin.readline())
# chat_list = list(map(str,sys.stdin.readline().split()))
chat_list = []
greet_count = 0

for i in range(chat_num):
    chat = sys.stdin.readline().strip()
    if chat != "ENTER":
        chat_list.append(chat)
    else:
        chat_list_set = set(chat_list)
        greet_count += len(chat_list_set)
        chat_list = []
        
chat_list_set = set(chat_list)
greet_count += len(chat_list_set)
chat_list = []
print(greet_count)