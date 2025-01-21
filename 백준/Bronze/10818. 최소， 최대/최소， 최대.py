N = int(input())
N_list = list(map(int, input().split()))

N_list = sorted(N_list)

result_max = N_list[0]
result_min = N_list[-1]

print(result_max, result_min)