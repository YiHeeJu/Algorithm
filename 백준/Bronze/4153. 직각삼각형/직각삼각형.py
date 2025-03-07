while True:
    n = list(map(int, input().split())) 
    v = [0,0,0]
    n.sort()
  
    if n == v:
        break
    elif n[0]**2 + n[1]**2 == n[2]**2:
        print("right")
    else :
        print("wrong")