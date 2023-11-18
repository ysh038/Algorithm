import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    command = sys.stdin.readline()
    command_front =command[0:1]

    if command_front == "1":
        trash, num = command.split()
        stack.append(num)
    elif command_front == "2":
        if len(stack) != 0:
            print(stack[len(stack)-1])
            stack.pop()
        else:
            print(-1)
    elif command_front == "3":
        print(len(stack))
    elif command_front == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    