N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    num = A + B
    print(f'Case {i+1}: {num}')