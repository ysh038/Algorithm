import sys

N = int(sys.stdin.readline())

def make(N):
    if N > 0:
        for width in range(N):
            for height in range(N):
                if (height >= int(N/3) and height < int((N/3)*2)) and (width >= int(N/3) and width < int((N/3)*2)):
                    print(" ",end="")
                else:
                    print("*",end="")
            print("")
        return make(int(N/3))
make(N)