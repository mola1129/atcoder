n, w = map(int, input().split())
weight = []
value = []
for _ in range(n):
    wi, vi = map(int, input().split())
    weight.append(wi)
    value.append(vi)
weight.append(0)
value.append(0)
dp = [[0] * (w + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(w + 1):
        if j - weight[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - weight[i]] + value[i])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
print(dp[n][w])
