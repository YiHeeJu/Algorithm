num_list = []
K = int(input())

for _ in range(K):
    N = int(input())
    if N == 0 :
        if num_list:
            num_list.pop()
    else :
        num_list.append(N)

if len(num_list) == 0 :
    print(0)
else :
    print(sum(num_list))