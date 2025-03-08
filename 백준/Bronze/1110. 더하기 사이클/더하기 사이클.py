count = 1

def num_count(x):
    if len(str(x)) == 1:
        num = x
    elif len(str(x)) == 2:
        num = [int(i) for i in str(x)]
        num = num[1]
    return num


n = list(map(int, input()))
if len(n) == 1:
    x = n[0]
    n = [0, x]
    

m=[0, 0]
m[0], m[1] = n[0], n[1]
n1 = n[1]
n2 = n[0] + n[1]
m[0] = n1
m[1] = n2

time = 0
while time != 1:
    if n != m:
        count += 1
        n1 = m[1]
        n2 = m[0] + m[1]
        n2 = num_count(n2)
        m[0] = n1
        m[1] = n2
    elif n == m :
        time = 1
        print(count)