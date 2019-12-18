n = int(input())
a = list(map(int, input().split()))
max_ans = 0
min_ans = 0
colors = [False] * 8
for i in range(n):
    rate = a[i]
    if 1 <= rate and rate < 400:
        colors[0] = True
    elif rate < 800:
        colors[1] = True
    elif rate < 1200:
        colors[2] = True
    elif rate < 1600:
        colors[3] = True
    elif rate < 2000:
        colors[4] = True
    elif rate < 2400:
        colors[5] = True
    elif rate < 2800:
        colors[6] = True
    elif rate < 3200:
        colors[7] = True
    else:
        max_ans += 1
min_ans += colors.count(True)
max_ans += colors.count(True)
print(max(min_ans, 1), max_ans)
