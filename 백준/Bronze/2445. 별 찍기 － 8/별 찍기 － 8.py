N = int(input())

count = 0
for i in range(1, N+1):
    stars = '*' * i
    spaces = ' ' * ((2*N) - (2*i))
    print(stars + spaces + stars)
    
for i in range(N-1, 0, -1):
    stars = '*' * i
    spaces = ' ' * ((2*N) - (2*i))
    print(stars + spaces + stars)