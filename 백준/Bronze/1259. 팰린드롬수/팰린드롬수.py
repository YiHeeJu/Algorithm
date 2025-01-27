while True:
    num = int(input())
    reverse = int(str(num)[::-1])
    if reverse == num and num != 0:
        print("yes")
    elif reverse != num :
        print("no")
    
    if num == 0 :
        break