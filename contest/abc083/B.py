n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    i = str(i)
    total = 0
    for j in i:
        total += int(j)
    if a <= total and total <= b:
        ans += int(i)
print(ans)
