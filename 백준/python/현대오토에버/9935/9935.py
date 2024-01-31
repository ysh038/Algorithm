import sys

string = input()
boom_string = input()

stack = []

for i in range(len(string)):
    stack.append(string[i])
    if "".join(stack[-len(boom_string):]) == boom_string:
        for _ in range(len(boom_string)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")