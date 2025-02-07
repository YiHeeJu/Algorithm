N = int(input())

def add(A, B):
    return A+B


for _ in range(N):
    A, B = map(int, input().split())
    print(add(A, B))