x = []
for _ in range(1, 11):
    n = int(input())
    x.append(n % 42)
    
print(len(list(set(x))))