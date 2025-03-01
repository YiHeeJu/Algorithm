hour, min, sec = map(int, input().split())
all_sec = int(input())
all_sec += 3600*hour + 60*min +sec

all_sec %= 86400

final_hour = all_sec // 3600
final_min = all_sec % 3600 // 60
final_sec = all_sec % 60
print(f'{final_hour} {final_min} {final_sec}')