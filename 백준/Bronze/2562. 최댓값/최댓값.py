# 10811
N_list = []

for i in range(9) :
    N = int(input())
    N_list.append(N)

N_list_t = sorted(N_list, reverse=True)
max = N_list_t[0]

for index, value in enumerate(N_list) :
    if value == max :
        index += 1
        break


print(f'{max}\n{index}')