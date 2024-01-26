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

