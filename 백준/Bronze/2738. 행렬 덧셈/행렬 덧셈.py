N, M = map(int, input().split())

arr_1 = []
arr_2 = []

for i in range(N):
    row = list(map(int, input().split()))
    arr_1.append(row)

for i in range(N) :
    row = list(map(int, input().split()))
    arr_2.append(row)

Matrix = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(arr_1[i][j] + arr_2[i][j])
    Matrix.append(row)


for low in Matrix :
    print(*low)