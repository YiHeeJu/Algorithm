T = int(input())

for _ in range(T):
    N = int(input())
    for _ in range(N):
        A,B = map(int, input().split())
        print(A+B, A*B)