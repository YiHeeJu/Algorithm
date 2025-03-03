num = int(input())*int(input())*int(input())
num = list(str(num))
num = list(map(int, num))
num.sort()
for i in range(10):
    print(num.count(i))