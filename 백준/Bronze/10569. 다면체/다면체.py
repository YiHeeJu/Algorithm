T=int(input())
for _ in range(T):
    V, E = map(int,input().split())
    M = 2 - V + E
    print(M)