
add_all = 0

def after(n):
    if n < 40 :
        num = 40
    else :
        num = n
    return num
    
for _ in range(5):
    score = int(input())

    add_all += after(score)
      

print(f'{add_all/5:.0f}')