import sys

N = int(sys.stdin.readline())

square = []
white_num = 0
blue_num = 0

for _ in range(N):
    square.append(list(map(int,sys.stdin.readline().split())))

def division(x,y,size):
    global white_num, blue_num
    color = square[x][y]

    for i in range(x,x+size):
        for j in range(y,y+size):
            if color != square[i][j]:
                division(x, y, size//2)
                division(x, y+size//2, size//2)
                division(x+size//2, y, size//2)
                division(x+size//2, y+size//2, size//2)
                return
    if color == 0:
        white_num += 1
    else:
        blue_num += 1

division(0,0,N)

print(white_num)
print(blue_num)