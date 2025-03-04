T = int(input())
for _ in range(T):
    N = str(input())
    N = list(N)
    num = 0
    
    for i in range(len(N)):
        if N[i] == "X":
            N[i] = 0
            num = 0
        elif N[i] == "O":
            num += 1
            N[i] = num
    print(sum(N))