n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += ((x >> i) & 1) * a[i]
print(ans)
