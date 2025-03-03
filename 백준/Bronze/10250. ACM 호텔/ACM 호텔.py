T = int(input())

for _ in range(T):
    count = 0
    H, W, N = map(int, input().split())

    for i in range(1, W+1):
        for j in range(1, H+1):
            count += 1
            room_num = j*100+i
            if count == N:
                print(room_num)
                
