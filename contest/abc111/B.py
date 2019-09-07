n = int(input())
ans = 0
for i in range(n, 1000):
    now = str(i)
    if now.count(now[0]) == 3:
        ans = i
        break
print(ans)
