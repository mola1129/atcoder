n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = 0
now = sum(p[:k-1])
for i in range(n - k + 1):
    now += p[i + k - 1]
    if now > ans:
        ans = now
    now -= p[i]
ans += k
ans /= 2
print(ans)
