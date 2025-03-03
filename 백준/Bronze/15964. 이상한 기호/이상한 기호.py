A, B = map(int, input().split())

def oper(A, B):
    operator = (A+B)*(A-B)
    return operator

print(oper(A, B))