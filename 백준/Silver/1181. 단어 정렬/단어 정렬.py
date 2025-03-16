N = int(input())
wl = []

def word(i):
    T = list(set(i))
    T.sort(key = lambda x : len(x))
    T = sorted(T, key=lambda x: (len(x), x))
    return T

for _ in range(N):
    wl.append(input())

ans = word(wl)
for i in range(len(ans)):
    print(ans[i])    