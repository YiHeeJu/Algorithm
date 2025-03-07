N = []
c = 0

a, b = map(int, input().split())

for i in range(1, 1001):
    j = 0
    while j < i:
        j += 1
        N.append(i)

for i in range(a-1, b):
    c += N[i]
print(c)