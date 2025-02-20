bill = {
    "Franklin":100,
    "Grant":50,
    "Jackson":20,
    "Hamilton":10,
    "Lincoln":5,
    "Washington":1}

n = int(input())
for _ in range(n):
    count = 0
    input_list = input().split()
    for name in input_list:
        if name in bill:
            count += bill[name]  
    print(f'${count}')