N,X=map(int, input().split())
A = list(map(int, input().split()))
B = []

for n in range(len(A)):
    if A[n] < X:
        B.append(A[n])
print(*B)