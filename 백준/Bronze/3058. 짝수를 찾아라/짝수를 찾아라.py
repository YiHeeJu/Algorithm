T = int(input())

for i in range(T):
    T_list = list(map(int, input().split()))

    result_data = [num for num in T_list if num % 2 == 0]
    total = sum(result_data)
  
    total_min = min(result_data)
    
    print(total, total_min)