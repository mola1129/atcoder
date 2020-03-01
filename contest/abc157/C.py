n, m = map(int, input().split())
sc = []
for _ in range(m):
    s, c = map(int, input().split())
    sc.append((s - 1, c))
for i in range(1000):
    now = str(i)
    l = len(now)
    if l != n:
        continue
    flag = True
    for s, c in sc:
        if s > l - 1:
            flag = False
            break
        if now[s] != str(c):
            flag = False
            break
    if flag:
        print(int(now))
        exit()
print(-1)
