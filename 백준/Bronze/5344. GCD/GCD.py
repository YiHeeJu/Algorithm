n = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for _ in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))
