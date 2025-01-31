H, M = map(int, input().split())

time = ( H*60 + M ) - 45

if time < 0 :
    W_H = 23
    W_M = 60 + time
else :
    W_H = time // 60
    W_M = time % 60


print(W_H, W_M)