S = int(input())

for _ in range(S):
    R, P = map(str, input().split())
    P = list(P)
    R = int(R)
    result = ""
    for i in range(len(P)):
        result += P[i] * R
    print(result)
