import sys

Number = int(sys.stdin.readline())

rect = []

def make(N):
    if N > 0:
        for width in range(Number):
            array = []
            for height in range(Number):
                if (height >= int(N/3) and height < int((N/3)*2)) and (width >= int(N/3) and width < int((N/3)*2)):
                    # print(" ",end="")
                    array.append(" ")
                else:
                    # print("*",end="")
                    array.append("*")
            array.append("\n")
            rect.append(array)
            # print("")
        if int(N/3) != 1:
            return make(int(N/3))
        
make(Number)

for i in range(Number):
    for j in range(Number):
        print(rect[i][j],end="")
    print("")