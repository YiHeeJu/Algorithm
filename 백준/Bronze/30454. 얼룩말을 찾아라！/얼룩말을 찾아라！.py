N, L = map(int, input().split())

def count(x):
    count = 0
    prev = 0
    for num in x:
        if num == 1 and prev == 0 :
            count += 1
        prev = num
    return count

Y = []

for _ in range(N):
    X = list(map(int, input()))
    Y.append(count(X))

print(max(Y), Y.count(max(Y))) 