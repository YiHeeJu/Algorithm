import sys

N = int(sys.stdin.readline())
stack = []
output = []

def program(A, B=None):
    if A == "push":
        stack.append(B)
    
    elif A == "pop":
        output.append(str(stack.pop() if stack else -1))

    elif A == "size":
        output.append(str(len(stack)))
    
    elif A == "empty":
        output.append("0" if stack else "1")
    
    elif A == "top":
        output.append(str(stack[-1] if stack else "-1"))
        


for _ in range(N):
    answer = sys.stdin.readline().split()
    if len(answer) == 2:
        program(answer[0], int(answer[1]))
    else:
        program(answer[0])
        
sys.stdout.write("\n".join(map(str, output)) + "\n")
