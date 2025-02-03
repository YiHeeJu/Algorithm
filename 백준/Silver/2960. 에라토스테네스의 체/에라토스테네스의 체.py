N, K = map(int, input().split())

is_prime = [True] * (N + 1)
count = 0 

for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i, N + 1, i):
            if is_prime[j]: 
                is_prime[j] = False 
                count += 1
                if count == K:
                    print(j)
                    exit()
