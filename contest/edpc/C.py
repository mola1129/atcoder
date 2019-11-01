n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j]: i-1日目に1つの行動を取った際の最大幸福度
dp = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            # 2回連続は不可
            if j == k:
                continue
            dp[i][k] = max(dp[i][k], dp[i - 1][j] + h[i - 1][k])
print(max(dp[n]))
