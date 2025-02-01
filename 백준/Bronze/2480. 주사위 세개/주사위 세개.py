A, B, C = map(int, input().split())

if A == B and B == C :
    answer = A*1000+10000
elif A == B or A == C :
    answer = A*100+1000
elif B == A or B == C :
    answer = B*100+1000
elif C == A and C == B :
    answer = C*100+1000
else :
    answer = max(A, B, C)*100

print(answer)