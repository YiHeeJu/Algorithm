N = int(input())
z = list(map(int, input().split()))
count = 0

def num(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True 

for i in range(N):
    if num(z[i]) == True:
        count += 1

print(count)