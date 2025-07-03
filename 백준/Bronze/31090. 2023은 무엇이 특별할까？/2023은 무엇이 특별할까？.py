for _ in range(int(input())):
    N = input()
    n = int(N[2:])
    N = int(N)
    
    print("Good" if (N+1) % n == 0 else "Bye")