while True :
    N, M = map(int, input().split())
    N_list = list(range(1, N+1))

    for i in range(M) :
        i, j = map(int, input().split())
        N_list[i-1:j] = N_list[i-1:j][::-1]

    break

print(*N_list)