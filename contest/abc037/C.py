n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = sum(a[:k])
now = ans
for i in range(n - k):
    now = now - a[i] + a[i + k]
    ans += now
print(ans)
