n = int(input())
shop = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
candidate = []
for i in range(1, 2 ** 10):
    is_open = [False] * 10
    cnt = [0] * n
    for j in range(10):
        if (i >> j) & 1:
            is_open[j] = True
    for k in range(n):
        for l in range(10):
            if is_open[l] and shop[k][l] == 1:
                cnt[k] += 1
    now_profit = 0
    for k in range(n):
        now_profit += p[k][cnt[k]]
    candidate.append(now_profit)
candidate.sort(reverse=True)
print(candidate[0])
