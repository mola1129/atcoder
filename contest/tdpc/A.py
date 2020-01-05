n = int(input())
p = list(map(int, input().split()))
p.append(0)
total = sum(p)
dp = [[False] * (total + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(total + 1):
        dp[i + 1][j] = dp[i + 1][j] or dp[i][j - p[i]]
        dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
ans = 0
for j in range(total + 1):
    for i in range(n + 1):
        if dp[i][j]:
            ans += 1
            break
print(ans)
