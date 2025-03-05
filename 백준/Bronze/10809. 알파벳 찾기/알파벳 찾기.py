al = [-1] * 26
S = input()
list(S)

for i, j in enumerate(S):
    index = ord(j) - ord('a')
    
    if al[index] == -1:
        al[index] = i
print(*al)