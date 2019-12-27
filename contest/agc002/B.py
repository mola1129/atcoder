n, m = map(int, input().split())
cnt = [1] * n
exist = [False] * n
exist[0] = True
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if exist[x]:
        exist[y] = True
        if cnt[x] == 1:
            exist[x] = False
    cnt[x] -= 1
    cnt[y] += 1
print(exist.count(True))
