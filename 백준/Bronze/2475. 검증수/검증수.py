a, b, c, d, e = map(int, input().split())


def goyou(a, b, c, d, e):
    num = ((a**2) + (b**2) + (c**2) + (d**2) + (e**2)) % 10
    return num

print(goyou(a, b, c, d, e))