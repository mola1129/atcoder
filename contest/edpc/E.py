n, w = map(int, input().split())
weight = []
value = []
for _ in range(n):
    wi, vi = map(int, input().split())
    weight.append(wi)
    value.append(vi)
weight.append(0)
value.append(0)
dp = [[float('inf')] * (10 ** 5 + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(10 ** 5 + 1):
        if j - value[i] >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - value[i]] + weight[i])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
for j in range(10 ** 5, -1, -1):
    if dp[n][j] <= w:
        print(j)
        break
