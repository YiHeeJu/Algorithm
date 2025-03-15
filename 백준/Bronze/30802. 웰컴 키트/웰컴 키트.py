N  = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())
Tshirt = 0

for i in range(len(shirt)):
    Tshirt += (shirt[i]+T-1)//T

print(Tshirt)
print(N // P, N % P)