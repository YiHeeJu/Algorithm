all_list = []
test = []
result = ""

for i in range(5):
    list_add = list(input())
    all_list.append(list_add)

for j in range(15):
    for i in range(5):
        if j < len(all_list[i]):
            test.append(all_list[i][j])
        else :
            test.append('')

for n in test:
    if n != '': 
        result += n
print(result)
