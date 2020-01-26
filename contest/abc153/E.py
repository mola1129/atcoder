h, n = map(int, input().split())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [float("inf")] * (2 * 10000 + 1)
dp[0] = 0
for i in range(h):
    for j in range(n):
        if (i + a[j]) > 2 * 10000:
            dp[2 * 10000] = min(dp[2 * 10000], dp[i] + b[j])
            continue
        dp[i + a[j]] = min(dp[i + a[j]], dp[i] + b[j])

ans = float('inf')
for j in range(h, 2 * 10000 + 1):
    ans = min(ans, dp[j])
print(ans)
