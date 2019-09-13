n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    total = 0
    for i in range(m):
        total += a[i] * b[i]
    total += c
    if total > 0:
        ans += 1
print(ans)
