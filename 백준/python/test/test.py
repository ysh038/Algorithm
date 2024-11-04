# N진수 만들기

# # 몇 진수로 만들지 입력받을 변수
# # 무한 반복
# while True:
#     JinSoo = int(input())
#     if JinSoo >= 1 and JinSoo <= 9:
#         # 1~9 사이의 정수가 입력되어야만 반복문이 종료된다.
#         break
#     print("1~9 사이의 정수만 입력해야 합니다.")

# # 입력받을 10진수 변수
# num = int(input())

# # 정답을 저장할 빈 문자열
# result = ""

# # N진수의 한 자리수는 N-1이 최대    ex) 10진수 정수 한 자리수의 최대값은 9, 2진수 정수 한 자리수의 최대값은 1
# # 10진수 정수를 N으로 더이상 나눌 수 없을 때 까지 나눈 후 마지막으로 남은 나머지를 거시기
# # 나눌 떄마다 result 에다가 붙인다!
# while num >= JinSoo - 1:
#     result += str(num % JinSoo)
#     num = num // JinSoo

# # N으로 나누고 마지막으로 남은 나머지를 result 뒤에 붙인다.
# result += str(num)
# print(result[::-1])
# ==========================================
# try:
#     H = input()  # 단, 입력 값은 H < 24인 0 이상의 정수
#     M = input()  # 단, 입력 값은 M <= 60인 0 이상의 정수

#     if M < 45:
#         if H == 0:
#             H = 23
#             M -= 45
#             M = 60 + M
#         else:
#             H -= 1
#             M -= 45
#             M = 60 + M
#     else:
#         M -= 45

#     print(H, M)
# except KeyboardInterrupt:
#     print("")

# ======= 아래는 이상한거

# if M < 45:
#     if H = "0":
#         H = 23
#         M =+ 60
#     else:
#         H =- 1
#         M =+ 60

# M =- 45
# print(H, M)

# total_muinutes = 60 * 60 + 0

# alarm_hours, alarm_minutes = divmod(total_muinutes,60)
# print(alarm_hours, alarm_minutes)
# def solution(board, k, ax, ay, bx, by):
#     answer = -2
#     for i in range(len(board)):
#         for j in range(len(board)):
#             # 폭탄의 폭발 범위를 전부 3으로 만들기
#             if board[j][i] == 1:
#                 for index in range(1,k+1):
#                     if j-index >= 0:
#                         if board[j-index][i] != 2 and board[j-index][i] != 1: 
#                             board[j-index][i] = 3 
#                         elif board[j-index][i] == 2: 
#                             break
#                 for index in range(1,k+1):
#                     if j+index < len(board):
#                         if board[j+index][i] != 2 and board[j+index][i] != 1:
#                             board[j+index][i] = 3
#                         elif board[j+index][i] == 2:
#                             break
#                 for index in range(1,k+1):
#                     if i-index >= 0:
#                         if board[j][i-index] != 2 and board[j][i-index] != 1:
#                             board[j][i-index] = 3
#                         elif board[j][i-index] == 2:
#                             break
#                 for index in range(1,k+1):
#                     if i+index < len(board):
#                         if board[j][i+index] != 2 and board[j][i+index] != 1:
#                             board[j][i+index] = 3
#                         elif board[j][i+index] == 2: 
#                             break

#     def is_valid_move(x, y):
#         return 0 <= x < len(board) and 0 <= y < len(board[0]) # and board[x][y] != 2

#     def is_safe(x, y):
#         return board[x][y] != 1 and board[x][y] != 3

#     def bfs(ax,ay,bx,by):
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         visited = set()
#         queue = [(ax,ay,bx,by,0)]
#         a_time = 0
#         print(queue)

#         while queue:
#             ax, ay, bx, by, time = queue.pop(0)

#             if (ax, ay) == (bx, by):
#                 continue

#             for dx, dy in directions:
#                 ax_next, ay_next = ax + dx, ay + dy
#                 bx_next, by_next = bx + dx, by + dy

#                 if (ax_next, ay_next, bx_next, by_next) in visited:
#                     continue
                
#                 if not is_valid_move(ax_next, ay_next) or not is_valid_move(bx_next, by_next):
#                     continue
                
#                 if not is_safe(ax_next, ay_next) or not is_safe(bx_next, by_next):
#                     continue
#                 a_time += 1
#                 visited.add((ax_next, ay_next, bx_next, by_next))
#                 queue.append((ax_next, ay_next, bx_next, by_next, time + 1))
#         return a_time
#     answer = bfs(ax,ay,bx,by)
#     return answer

x = 'a','b'
print(x)

L = ['c','d']

L.append(x)
print(L)

L+='e','f'
print(L)

L+=['g','h']
print(L)