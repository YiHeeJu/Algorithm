X = int(input())
N = int(input())
count = 0

for _ in range(N):
    a, b = map(int, input().split())
    count += a*b

if X == count:
    print("Yes")
else :
    print("No")