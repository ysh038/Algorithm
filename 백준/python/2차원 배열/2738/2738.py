N, M = map(int,input().split())

matrix1,matrix2 = [] , []

for row in range(N):
    row = list(map(int,input().split()))
    matrix1.append(row)

for row in range(N):
    row = list(map(int,input().split()))
    matrix2.append(row)

result_matrix = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
        print(result_matrix[i][j], end=" ")
    print()