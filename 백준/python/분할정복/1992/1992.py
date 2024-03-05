import sys

N = int(sys.stdin.readline())
video = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def conquer(x,y,size):
    check = video[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if check != video[i][j]:
                check = -1
                break
    
    if check == -1:
        print("(",end="")
        conquer(x,y,size//2)
        conquer(x,y+size//2,size//2)
        conquer(x+size//2,y,size//2)
        conquer(x+size//2,y+size//2,size//2)
        print(")",end="")
    elif check == 0:
        print("0",end="")
    else:
        print("1",end="")
    return


conquer(0,0,N)