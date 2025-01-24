A, B = map(int, input().split())
C = int(input())

cooking = ((A*60) + B + C )

hour = cooking // 60
minute = cooking % 60

if hour >= 24:
    hour -=24
else :
    pass


print(hour, minute)