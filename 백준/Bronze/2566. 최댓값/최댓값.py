Matrix = []

for i in range(9):
    num = list(map(int, input().split()))
    Matrix.append(num)

target = max(map(max, Matrix))

for i, num in enumerate(Matrix):
    if target in num :
        row = i
        col = num.index(target)
        break

print(target)
print(row+1, col+1)