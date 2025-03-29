N = int(input())

for i in range(N):
    i += 1
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')