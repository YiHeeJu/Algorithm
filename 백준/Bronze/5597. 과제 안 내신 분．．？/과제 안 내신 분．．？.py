stu_num=[]
for i in range(28):
    stu_num.append(int(input()))
for i in range(1, 31):
    if i not in stu_num:
        print(i)
