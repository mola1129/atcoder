h, n = map(int, input().split())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [float("inf")] * (h + 1)
dp[0] = 0
for i in range(h):
    for j in range(n):
        index = min(i + a[j], h)
        dp[index] = min(dp[index], dp[i] + b[j])

print(dp[h])
