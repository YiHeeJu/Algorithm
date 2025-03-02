N = int(input())
list_num = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(len(list_num)):
    if list_num[i] == v:
        count += 1
print(count)