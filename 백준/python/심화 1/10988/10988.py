# array = input()
# cnt=0

# for i in range(len(array)//2):
#     if array[i] == array[len(array)-(i+1)]:
#         cnt += 1
#         continue
#     else:
#         print(0)
#         break

# if cnt == len(array)//2:
#     print(1)

array = list(str(input()))
if list(reversed(array)) == array:
    print(reversed(array))
    print(1)
else:
    print(0)